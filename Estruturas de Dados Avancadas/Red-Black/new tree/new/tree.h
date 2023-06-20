#ifndef TREE_H
#define TREE_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct no {
    int imdb;
    int color;
    int qntMovies;
    int *movies;
    struct no *parent;
    struct no *left;
    struct no *right;
} No;

typedef struct tree {
    No *root;
} Tree;

Tree *initTree();
void insertNo(Tree *tree, int imdb, char *movies);
No *createNo(int imdb, char *movies);
No *insert(No *root, No *no);
void fixTree(Tree *tree, No *no);
void rotateRight(Tree *tree, No *no);
void rotateLeft(Tree *tree, No *no);
void getNames(Tree *tree, char *filename);
void freeTree(Tree *tree);
void freeNo(No *no);

#endif