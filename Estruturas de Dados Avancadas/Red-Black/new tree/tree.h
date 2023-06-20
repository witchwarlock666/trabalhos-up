#ifndef TREE_H
#define TREE_H

typedef struct no {
    int imdb;
    int color;
    int *movies;
    struct no *parent;
    struct no *left;
    struct no *right;
} No;

typedef struct tree {
    No *root;
} Tree;

Tree *initTree();
void insertNo(Tree *tree, int imdb);
No *createNo(int imdb);
No *insert(No *root, No *no);
void fixTree(Tree *tree, No *no);
void rotateRight(Tree *tree, No *no);
void rotateLeft(Tree *tree, No *no);

#endif