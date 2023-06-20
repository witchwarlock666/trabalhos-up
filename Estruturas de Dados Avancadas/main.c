#define _CRT_SECURE_NO_WARNINGS
// #include "graph.c"
#include "tree.c"
#include "graph.c"

void p(Graph *graph, No *no, char *title) {
    if (!no) return;

    p(graph, no->left, title);
    p(graph, no->right, title);

    int *movieList = no->movies;

    for (int i = 0; i < no->qntMovies; i++) {
        int c = insertMovie(graph, movieList[i], "movies.tsv", &title);
        if (c) {
            insertNode(graph, movieList[i], title);
        }
        else {
            movieList[i] = 0;
        }
    }
    for (int i = 0; i < no->qntMovies; i++) {
        if (movieList[i]) {
            for (int j = 0; j < no->qntMovies; j++) {
                if (movieList[j]) imdbConnect(graph, movieList[i], movieList[j]);
            }
        }
    }
}

int main() {
    Graph *graph = initGraph();
    // insertMovie(graph, 53137, "movies.tsv");
    Tree *tree = initTree();

    // getMovies(graph, "movies.tsv");
    getNames(tree, "actors.tsv");
    // filePrint(tree->root);
    // printTree(tree->root);
    char *title = (char *)malloc(sizeof(char)*400);

    p(graph, tree->root, title);

    // int *movieList = (int *)malloc(sizeof(int));
    // int *size = calloc(sizeof(int), 1);
    // movieList = createNodes(graph, tree->root, movieList, size);
    
    // for (int i = 0; i < *size; i++) {
    //     title = insertMovie(graph, movieList[i], "movies.tsv");
    //     if (title) {
    //         insertNode(graph, movieList[i], title);
    //     }
    //     else {
    //         movieList[i] = 0
    //     }
    // }
    // for (int i = 0; i < *size; i++) {
    //     for (int j = 0; j < *size; j++) {
    //         imdbConnect(graph, movieList[i], movieList[j]);
    //     }
    // }
    

    // printTree(tree->root);

    // printGraph2(graph);

    // insertNode(graph, 1, "aa");
    // insertNode(graph, 2, "bb");
    // insertNode(graph, 3, "cc");
    // insertNode(graph, 4, "dd");

    // imdbConnect(graph, 1, 2);
    // imdbConnect(graph, 1, 3);
    // imdbConnect(graph, 2, 3);
    // imdbConnect(graph, 3, 4);
    // imdbConnect(graph, 1, 1);

    printGraph(graph);

    freeGraph(graph);
    freeTree(tree);
}