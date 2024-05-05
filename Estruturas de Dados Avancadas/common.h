#ifndef COMMON_H
#define COMMON_H

#include "tree.h"
#include "graph.h"


void getMovies(Graph *graph, char *filename, Tree *tree);
void printNode(Node *node, FILE *file, Tree *tree);
void printGraph(Graph *graph, Tree *tree);
Node *getNodeTree(No *no, int imdb);

#endif