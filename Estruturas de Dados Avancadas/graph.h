#ifndef GRAPH_H
#define GRAPH_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tree.h"

// Graph node struct
typedef struct node {
    int imdb;
    char *title;
    int printed;
    int year;
    int index;
    int n_neighbors;
    int *neighbors;
} Node;

// Graph struct
typedef struct graph {
    int n_nodes;
    Node **nodes;
} Graph;

void freeGraph(Graph *graph);
Node *createNode(int imdb, char *label, int year);
void imdbConnect(Graph *graph, Node *node1, Node *node2);
void connect(Node *node1, Node *node2);
void connectNodes(Node *a, Node *b);
Graph *initGraph();
void addNode(Graph *graph, Node *node);
Node *insertNode(Graph *graph, int imdb, char *label, int year);
Node *getNode(Graph *graph, int imdb);
int exists(Graph *graph, int imdb);
void printGraph2(Graph *graph);
int insertMovie(Graph *graph, int imdb, char *filename, char **title);

#endif