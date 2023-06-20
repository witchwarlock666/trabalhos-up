#include <stdio.h>
#include <stdlib.h>

struct node {
    int vertex;
    int imdb;
    struct node *next;
};

struct edge {
    
}

struct Graph {
    int numVertices;
    struct node **nodes;
    struct node **adjLists;
};

// Create a node
struct node *createNode(struct Graph *graph) {
    struct node *newNode = malloc(sizeof(struct node));
    if (newNode == NULL) return NULL;
    newNode->vertex = graph->numVertices;
    newNode->next = NULL;
    newNode->imdb = 0;

    graph->nodes = realloc(graph->nodes, sizeof(graph->nodes) + sizeof(struct node*));
    graph->adjLists = realloc(graph->adjLists, sizeof(graph->adjLists) + sizeof(struct node*));
    graph->nodes[graph->numVertices] = newNode;
    graph->numVertices += 1;
    return newNode;
}

// Create a graph
struct Graph *createAGraph(int vertices) {
    struct Graph *graph = malloc(sizeof(struct Graph));
    graph->numVertices = 0;

    graph->adjLists = NULL;
    graph->nodes = NULL;

    return graph;
}

int findNode(struct Graph *graph, int imdb) {
    for (int i = 0; i < graph->numVertices; i++) {
        if (graph->nodes[i]->imdb == imdb) {
            return i;
        }
    }

    return -1;
}

// Add edge
void addEdge(struct Graph *graph, int s, int d) {
    // Add edge from s to d
    struct node *newNode = createNode(graph);
    newNode->next = graph->adjLists[s];
    graph->adjLists[s] = newNode;

    // Add edge from d to s
    newNode = createNode(graph);
    newNode->next = graph->adjLists[d];
    graph->adjLists[d] = newNode;
}

// Print the graph
void printGraph(struct Graph *graph) {
    int v;
    for (v = 0; v < graph->numVertices; v++) {
        struct node *temp = graph->adjLists[v];
        printf("\n Vertex %d\n: ", v);
        while (temp) {
            printf("%d -> ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}