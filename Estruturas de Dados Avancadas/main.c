#define _CRT_SECURE_NO_WARNINGS
// #include "graph.c"

#include "common.c"

#include "tree.c"
#include "graph.c"
// #include "graph.c"

void p(Graph *graph, No *no, char *title, Tree *tree) {
    if (!no) return;

    p(graph, no->left, title, tree);
    p(graph, no->right, title, tree);

    int *movieList = no->movies;

    for (int i = 0; i < no->qntMovies; i++) {
        Node *node = getNodeTree(tree->root, movieList[i]);
        if (!node) {
            int c = insertMovie(graph, movieList[i], "movies.tsv", &title);
            if (c == 1) {
                node = insertNode(graph, movieList[i], title);
                insertNoGraph(tree, movieList[i], node);
            }
            else {
                movieList[i] = 0;
            }
        }
        
        
    }
    for (int i = 0; i < no->qntMovies; i++) {
        if (movieList[i]) {
            for (int j = 0; j < no->qntMovies; j++) {
                if (movieList[j]) {
                    Node *node1 = getNodeTree(tree->root, no->movies[i]);
                    Node *node2 = getNodeTree(tree->root, no->movies[j]);
                    if (!node1 || !node2) continue;
                    imdbConnect(graph, node1, node2);
                }
            }
        }
    }
    if (no->imdb % 1000000 == 0)printf("%d\n", no->imdb);
}

int main() {
    Graph *graph = initGraph();
    // insertMovie(graph, 53137, "movies.tsv");
    Tree *tree = initTree();
    Tree *graphTree = initTree();

    // getMovies(graph, "movies.tsv");
    getMovies(graph, "movies.tsv", graphTree);
    getNames(tree, "actors.tsv");
    // for (int i =0; i < graph->n_nodes; i++) {
    //     insertNoGraph(graphTree, graph->nodes[i]->imdb, graph->nodes[i]);
    // }
    // filePrint(tree->root);
    // printTree(tree->root);
    char *title = (char *)malloc(sizeof(char)*400);

    p(graph, tree->root, title, graphTree);

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