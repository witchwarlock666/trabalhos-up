#include "tree.h"

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

Tree *initTree() {
    Tree *tree = (Tree *)malloc(sizeof(Tree));
    tree->root = (No *)malloc(sizeof(No));
    return tree;
}

No *createNo(int imdb, char *movies) {

    int *titles = (int *)malloc(sizeof(int));
    int idMovie = atoi(strtok(movies, ",") + 2);
    titles[0] = idMovie;
    int qntMovies = 1;

    char *idMovieStr = strtok(NULL, ",");

    if (idMovieStr != NULL){
        idMovie = atoi(idMovieStr + 2);
    }
    
    while(idMovieStr != NULL){
        qntMovies++;
        titles = (int *)realloc(titles, (qntMovies*sizeof(int)));
        titles[qntMovies-1] = idMovie;
        idMovieStr = strtok(NULL, ",");

        if (idMovieStr != NULL){
            idMovie = atoi(idMovieStr + 2);
        }
    }

    No *no = (No *)malloc(sizeof(No));
    no->imdb = imdb;
    no->color = 1;
    no->qntMovies = qntMovies;
    no->movies = titles;
    no->parent = NULL;
    no->left = NULL;
    no->right = NULL;
    return no;
}

void insertNo(Tree *tree, int imdb, char *movies) {
    No *no = createNo(imdb, movies);
    if (tree->root->color < 0) {
        no->color = 0;
        tree->root = no;
        return;
    }
    insert(tree->root, no);
    fixTree(tree, no);
}

No *insert(No *root, No *no) {
    if (!root) {
        return NULL;
    }

    if (no->imdb < root->imdb) {
        if (!insert(root->left, no)) {
            no->parent = root;
            root->left = no;
        }
    }
    else {
        if (!insert(root->right, no)) {
            no->parent = root;
            root->right = no;
        }
    }

    return no;
}

void fixTree(Tree *tree, No *no) {
    No *current = (No *)malloc(sizeof(No));
    current = no;
    tree->root->color = 0;
    if (no == tree->root) return;
    No *p = current->parent;;
    No *gp = p->parent;
    while (current != tree->root && current->parent->color == 1) {
        p = current->parent;
        gp = p->parent;
        if (p == gp->left) {
            No *unc = gp->right;
            if (unc != NULL && unc->color) {
                gp->color = 1;
                p->color = 0;
                unc->color = 0;
                current = gp;
            }
            else {
                if (current == p->right) {
                    rotateLeft(tree, p);
                    current = p;
                }
                else {
                    rotateRight(tree, gp);
                    int c = p->color;
                    p->color = gp->color;
                    gp->color = c;
                    current = gp;
                }
            }
        }
        else {
            No *unc = gp->left;
            if (unc != NULL && unc->color) {
                gp->color = 1;
                p->color = 0;
                unc->color = 0;
                current = gp;
            }
            else {
                if (current == p->left) {
                    rotateRight(tree, p);
                    current = p;
                }
                else {
                    rotateLeft(tree, gp);
                    int c = p->color;
                    p->color = gp->color;
                    gp->color = c;
                    current = gp;
                }
            }
        }
        tree->root->color = 0;
    }
}

void rotateLeft(Tree *tree, No *no) {
    No *right = no->right;
    no->right = right->left;
    if (right->left) {
        right->left->parent = no;
    }
    right->parent = no->parent;
    if (!no->parent) {
        tree->root = right;
    }
    else if (no == no->parent->left) {
        no->parent->left = right;
    }
    else {
        no->parent->right = right;
    }
    right->left = no;
    no->parent = right;
}

void rotateRight(Tree *tree, No *no) {
    No *left = no->left;
    no->left = left->right;
    if (left->right) {
        left->right->parent = no;
    }
    left->parent = no->parent;
    if (!no->parent) {
        tree->root = left;
    }
    else if (no == no->parent->right) {
        no->parent->right = left;
    }
    else {
        no->parent->left = left;
    }
    left->right = no;
    no->parent = left;
}

void freeTree(Tree *tree) {
    freeNo(tree->root);
    free(tree);
}

void freeNo(No *no) {
    if (!no) return;
    freeNo(no->left);
    freeNo(no->right);
    free(no);
    return;
}

void printTree(struct no* root) {
    if (root == NULL)
        return;
    printf("[ ");
    printTree(root->left);
    printf(root->color == 1 ? "\033[31m%d\033[0m" :  "\033[34m%d\033[0m", root->imdb);
    printTree(root->right);
    printf(" ]");
}

void getNames(Tree *tree, char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Erro!");
        return;
    }
    char *buffer = (char *)malloc(sizeof(char) * 200);
    fgets(buffer, 105, file);

    int i = 0;
    char *imdbstr;
    int imdb;
    char *titles;
    char *trash;

    while (i < 22) {
        fgets(buffer, 400, file);
        imdbstr = strtok(buffer, "\t");
        imdb = atoi(imdbstr + 2);

        trash = strtok(NULL, "\t");
        if (trash == NULL) continue;

        trash = strtok(NULL, "\t");
        if (trash == NULL) continue;

        trash = strtok(NULL, "\t");
        if (trash == NULL) continue;

        trash = strtok(NULL, "\t");
        if (trash == NULL) continue;

        titles = strtok(NULL, "\t");
        if (titles == NULL) continue;

        insertNo(tree, imdb, titles);
        ++i;
        printf("%d - %d\n", i, imdb);
    }

    // Close the file
    fclose(file);

    // Free the allocated memory
    free(buffer);
}