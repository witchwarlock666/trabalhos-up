#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "graph.h"

// Clear graph from memory
void freeGraph(Graph *graph) {
    int i;
    for(i=0; i<graph->n_nodes; i++) {
        free(graph->nodes[i]);
    }

    free(graph->nodes);
    free(graph);
}

// Create a node with imdb Id and movie title
Node *createNode(int imdb, char *title) {
    Node *node = (Node *)calloc(sizeof(Node), 1);
    node->imdb = imdb;
    char *str = malloc(sizeof(char) * 400);
    strcpy(str, title);
    node->title = str;
    node->n_neighbors = 0;
    node->neighbors = (int *)malloc(node->n_neighbors*sizeof(int));
    return node;
}

// Connect 2 nodes
void connectNodes(Node *a, Node *b) {
    a->neighbors = (int *)realloc(a->neighbors, (a->n_neighbors+1)*sizeof(int));
    a->neighbors[a->n_neighbors] = b->imdb;
    a->n_neighbors += 1;
}

// Returns node based on imdb Id search
Node *getNode(Graph *graph, int imdb) {
    int i;
    Node *node;
    for(i = 0; i < graph->n_nodes; i++) {
        node = graph->nodes[i];
        if(node->imdb == imdb) {
            return node;
        }
    }
    return NULL;
}

// Checks if node exists
int exists(Graph *graph, int imdb) {
    return getNode(graph, imdb) != NULL;
}

// Makes a two way connection between nodes
void connect(Node *node1, Node *node2) {
    connectNodes(node1, node2);
    connectNodes(node2, node1);
}

// Connects 2 nodes based on their imdb Id
void imdbConnect(Graph *graph, int imdb1, int imdb2) {
    Node *node1 = getNode(graph, imdb1);
    Node *node2 = getNode(graph, imdb2);

    if (strcmp(node1->title, "1984") == 0 || strcmp(node2->title, "1984") == 0) {
        printf("");
    }

    if (node1 == node2) return;

    for (int i = 0; i < node1->n_neighbors; i++) {
        if (node1->neighbors[i] == node2->imdb) {
            return;
        }
    }
    for (int i = 0; i < node2->n_neighbors; i++) {
        if (node2->neighbors[i] == node1->imdb) {
            return;
        }
    }

    connect(node1, node2);
}

// Initializes the graph
Graph *initGraph() {
    Graph *graph = (Graph *)malloc(sizeof(Graph));
    graph->n_nodes = 0;
    graph->nodes = NULL;
    return graph;
}

// Add node to graph
void addNode(Graph *graph, Node *node) {
    graph->nodes = (Node **)realloc(graph->nodes,
                                    (graph->n_nodes+1)*sizeof(Node *));

    graph->nodes[graph->n_nodes] = node;
    graph->n_nodes += 1;
}

// Create node and insert it in the graph
void insertNode(Graph *graph, int imdb, char *title) {
    if (!exists(graph, imdb)) {
        Node *node = createNode(imdb, title);
        addNode(graph, node);
    }
}

// Dot language node print
void printNode(Graph *graph, Node *node, Node **list, int n, FILE *file) {
    int i;
    int cont;
    for(i=0; i<node->n_neighbors; i++) {
        Node *neighbor = getNode(graph, node->neighbors[i]);
        cont = 1;
        for (int j = 0; j < n; j++) {
            if (list[j] == neighbor) {
                cont = 0;
            }
            if (!cont) break;
        }
        if (cont) {
            fprintf(file, "\"%d - %s\" -- ", node->imdb, node->title);
            fprintf(file, "\"%d - %s\"\n", node->imdb, neighbor->title);
        }
    }
}

// Dot language graph print
void printGraph(Graph *graph) {
    FILE *file = fopen("graph.dot", "w");
    if (!file) {
        return;
    }

    int i;
    fprintf(file, "graph {\n");
    Node **list = malloc(sizeof(Node*) * graph->n_nodes);
    for(i=0; i<graph->n_nodes; i++) {
        list[i] = graph->nodes[i];
        printNode(graph, graph->nodes[i], list, graph->n_nodes, file);
    }
    fprintf(file, "}\n");
    fclose(file);
    free(list);
}

// Prints all nodes in graph for debug
void printGraph2(Graph *graph) {
    for(int i=0; i<graph->n_nodes; i++) {
        printf("%d - %s\n", graph->nodes[i]->imdb, graph->nodes[i]->title);
    }
}

// Gets movies from file and inserts in graph
void getMovies(Graph *graph, char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Erro!");
        return;
    }
    char *buffer = malloc(sizeof(char) * 200);
    fgets(buffer, 105, file);

    int i = 0;
    char *imdbstr;
    int imdb;
    char *type;
    char *title;

    while (i < 50) {
        fgets(buffer, 400, file);
        imdbstr = strtok(buffer, "\t");
        imdb = atoi(imdbstr + 2);

        type = strtok(NULL, "\t");
        if (type == NULL) continue;

        title = strtok(NULL, "\t");
        if (title == NULL) continue;

        if (strcmp(type, "movie") == 0) {
            insertNode(graph, imdb, title);
            ++i;
            printf("%d - %d\n", i, imdb);
        }
    }
}

int insertMovie(Graph *graph, int imdb, char *filename, char **title) {
    if (exists(graph, imdb)) {
        return 0;
    }

    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Erro - %d\n", imdb);
        return 0;
    }
    char *buffer = malloc(sizeof(char) * 400);
    fgets(buffer, 105, file);

    char *imdbstr;
    int imdb1;
    char *type;
    while (!feof(file)) {
        fgets(buffer, 400, file);
        imdbstr = strtok(buffer, "\t");
        imdb1 = atoi(imdbstr + 2);
        if (imdb1 != imdb ) {
            continue;
        }

        type = strtok(NULL, "\t");
        if (type == NULL) continue;

        *title = strtok(NULL, "\t");
        if (title == NULL) continue;

        if (strcmp(type, "movie") == 0) {
            fclose(file);
            return 1;
        }
        fclose(file);
        return 0;
    }
    fclose(file);
    return 0;
}