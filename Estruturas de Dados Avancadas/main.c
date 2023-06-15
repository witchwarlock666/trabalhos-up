#include "graph.h"

int main() {
    struct Graph *graph = createAGraph(4);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 0, 3);
    addEdge(graph, 1, 2);

    printGraph(graph);

    int a;

    scanf("%d", &a);
    return 0;
}