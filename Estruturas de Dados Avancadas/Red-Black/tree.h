#ifndef TREE_H
#define TREE_H


struct no {
    int imdb;              // Dado
    int color;             // 1-vermelho, 0-preto
    struct no* parent;   // Pai
    struct no* right;    // Filho direito
    struct no* left;     // Filho esquerdo
    int *movies;
};

struct no* init_tree();
struct no* insert(struct no* current, struct no* no);
struct no* create(struct no* root, int imdb);
void rotate_right(struct no* temp, struct no* root);
void rotate_left(struct no* temp, struct no* root);
void fixup(struct no* root, struct no* pt);
void print_tree(struct no* root);
void free_tree(struct no* root);

#endif