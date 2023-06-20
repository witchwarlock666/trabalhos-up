#ifndef GRAPH_H
#define GRAPH_H

// Graph node struct
typedef struct node {
    int imdb;
    char *title;
    int n_neighbors;
    int *neighbors;
} Node;

// Graph struct
typedef struct graph {
    int n_nodes;
    Node **nodes;
} Graph;

// Function prototypes
void freeGraph(Graph *graph);
Node *createNode(int imdb, char *label);
void imdbConnect(Graph *graph, int imdb1, int imdb2);
void connect(Node *node1, Node *node2);
void connectNodes(Node *a, Node *b);
Graph *initGraph();
void addNode(Graph *graph, Node *node);
void insertNode(Graph *graph, int imdb, char *label);
Node *getNode(Graph *graph, int imdb);
int exists(Graph *graph, int imdb);
void printNode(Graph *graph, Node *node, Node **list, int n);
void printGraph(Graph *graph);
void printGraph2(Graph *graph);
void getMovies(Graph *graph, char *filename);
Node *insertMovie(Graph *graph, int imdb, char *filename);

#endif