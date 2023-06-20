#include "tree.h"

#include <stdio.h>
#include <stdlib.h>

struct no* init_tree(int imdb) {
    struct no *no = (struct no *)malloc(sizeof(struct no));
    no->imdb = imdb;
    no->color = 0;
    no->left = NULL;
    no->right = NULL;
    no->parent = NULL;
    no->movies = (int *)malloc(sizeof(int));
}

struct no* insert(struct no* current, struct no* no) {
    if (current == NULL) return no;

    if (no->imdb < current->imdb) {
        current->left = insert(current->left, no);
        current->left->parent = current;
    } else if (no->imdb > current->imdb) {
        current->right = insert(current->right, no);
        current->right->parent = current;
    }

    return current;
}

struct no* create(struct no* root, int imdb) {
    struct no* no = (struct no*)malloc(sizeof(struct no));
    no->imdb = imdb;
    no->color = 1;
    no->parent = NULL;
    no->left = NULL;
    no->right = NULL;
    no->movies = (int*)malloc(sizeof(int));

    insert(root, no);
    fixup(root, no);

    return no;
}

// Função para realizar a rotação à direita do nó passado
void rotate_right(struct no* temp, struct no* root) {
    struct no* left = temp->left;
    temp->left = left->right;
    if (temp->left)
        temp->left->parent = temp;
    left->parent = temp->parent;
    if (!temp->parent)
        root = left;
    else if (temp == temp->parent->left)
        temp->parent->left = left;
    else
        temp->parent->right = left;
    left->right = temp;
    temp->parent = left;
}

// Função para realizar a rotação à esquerda do nó passado
void rotate_left(struct no* temp, struct no* root) {
    struct no* right = temp->right;
    temp->right = right->left;
    if (temp->right)
        temp->right->parent = temp;
    right->parent = temp->parent;
    if (!temp->parent)
        root = right;
    else if (temp == temp->parent->left)
        temp->parent->left = right;
    else
        temp->parent->right = right;
    right->left = temp;
    temp->parent = right;
}

// Função para corrigir violações causadas pela inserção na BST
void fixup(struct no* root, struct no* pt) {
    struct no* parent_pt = NULL;
    struct no* grand_parent_pt = NULL;

    while ((pt != root) && (pt->color != 0) && (pt->parent->color == 1)) {
        parent_pt = pt->parent;
        grand_parent_pt = pt->parent->parent;

        // Caso A: O pai de pt é o filho esquerdo do avô de pt
        if (parent_pt == grand_parent_pt->left) {
            struct no* uncle_pt = grand_parent_pt->right;

            // Caso 1: O tio de pt também é vermelho
            if (uncle_pt != NULL && uncle_pt->color == 1) {
                grand_parent_pt->color = 1;
                parent_pt->color = 0;
                uncle_pt->color = 0;
                pt = grand_parent_pt;
            } 
            else {
                // Caso 2: pt é o filho direito de seu pai
                if (pt == parent_pt->right) {
                    rotate_left(parent_pt, root);
                    pt = parent_pt;
                    parent_pt = pt->parent;
                    root = parent_pt;
                } 
                else {
                    // Caso 3: pt é o filho esquerdo de seu pai
                    rotate_right(grand_parent_pt, root);
                    int t = parent_pt->color;
                    parent_pt->color = grand_parent_pt->color;
                    grand_parent_pt->color = t;
                    pt = parent_pt;
                    root = grand_parent_pt;
                }
            }
        } 
        else {
            // Caso B: O pai de pt é o filho direito do avô de pt
            struct no* uncle_pt = grand_parent_pt->left;

            // Caso 1: O tio de pt também é vermelho
            if ((uncle_pt != NULL) && (uncle_pt->color == 1)) {
                grand_parent_pt->color = 1;
                parent_pt->color = 0;
                uncle_pt->color = 0;
                pt = grand_parent_pt;
            } 
            else {
                // Caso 2: pt é o filho esquerdo de seu pai
                if (pt == parent_pt->left) {
                    rotate_right(parent_pt, root);
                    pt = parent_pt;
                    parent_pt = pt->parent;
                    root = parent_pt;
                } 
                else {
                    // Caso 3: pt é o filho direito de seu pai
                    rotate_left(grand_parent_pt, root);
                    int t = parent_pt->color;
                    parent_pt->color = grand_parent_pt->color;
                    grand_parent_pt->color = t;
                    pt = parent_pt;
                    root = grand_parent_pt;
                }
            }
        }
    }

    root->color = 0;
}

// Função para imprimir em ordem a árvore
void print_tree(struct no* root) {
    if (root == NULL)
        return;
    print_tree(root->left);
    printf("%d ", root->imdb);
    print_tree(root->right);
}

// Função para liberar a memória alocada para a árvore
void free_tree(struct no* root) {
    if (root == NULL)
        return;
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}
