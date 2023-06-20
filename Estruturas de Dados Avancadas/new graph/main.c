#define _CRT_SECURE_NO_WARNINGS
#include "graph.c"

int main() {
    Graph *graph = initGraph();

    // getMovies(graph, "movies.tsv");
    // printGraph2(graph);

    insertNode(graph, 1, "aa");
    insertNode(graph, 2, "bb");
    insertNode(graph, 3, "cc");
    insertNode(graph, 4, "dd");

    imdbConnect(graph, 1, 2);
    imdbConnect(graph, 1, 3);
    imdbConnect(graph, 2, 3);
    imdbConnect(graph, 3, 4);

    printGraph(graph);

    freeGraph(graph);
}