#include "common.h"

void getMovies(Graph *graph, char *filename, Tree *tree) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Erro!");
        return;
    }
    char *buffer = malloc(sizeof(char) * 400);
    fgets(buffer, 105, file);

    // int i = 0;
    char *imdbstr;
    int imdb;
    char *type;
    char *title;
    char *isAdultStr;
    int isAdult;
    char *yearStr;
    int year;

    printf("Gerando grafo...\n");

    while (!feof(file)) {
        fgets(buffer, 400, file);
        imdbstr = strtok(buffer, "\t");
        imdb = atoi(imdbstr + 2);

        if (imdb == 64846) {
            printf("");
        }

        type = strtok(NULL, "\t");
        if (type == NULL) continue;

        title = strtok(NULL, "\t");
        if (title == NULL) continue;

        type = strtok(NULL, "\t");
        if (type == NULL) continue;
        
        isAdultStr = strtok(NULL, "\t");
        if (isAdultStr == NULL) continue;
        isAdult = atoi(isAdultStr);
        
        yearStr = strtok(NULL, "\t");
        if (yearStr == NULL) continue;
        year = atoi(yearStr);

        if (isAdult) {
            // printf("%s\n", title);
            insertNoGraph(tree, imdb, insertNode(graph, imdb, title, year));
            // ++i;
            // if (i % 100000 == 0) {
            //     printf("%d - %d\n", i, imdb);
            // }
        }
    }
    printf("done");
}

/*
tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres
tt0000001	short	Carmencita	Carmencita	0	1894	\N	1	Documentary,Short
*/

Node *getNodeTree(No *no, int imdb) {
    if (!no) return NULL;

    if (imdb < no->imdb) return getNodeTree(no->left, imdb);
    if (imdb > no->imdb) return getNodeTree(no->right, imdb);
    if (imdb == no->imdb) return no->node;
    return NULL;
}

void printNode(Node *node, FILE *file, Tree *tree) {
    int i;
    int cont;
    for(i=0; i<node->n_neighbors; i++) {
        node->printed = 1;
        Node *neighbor = getNodeTree(tree->root, node->neighbors[i]);
        if (neighbor->printed) continue;
        
        fprintf(file, "\"%d - %s\" -- ", node->imdb, node->title);
        fprintf(file, "\"%d - %s\"\n", neighbor->imdb, neighbor->title);
    }
}

// Dot language graph print
void printGraph(Graph *graph, Tree *tree) {
    FILE *file = fopen("graph2.dot", "w");
    if (!file) {
        return;
    }
    printf("Gerando arquivo DOT...\n");
    int i;
    fprintf(file, "graph {\n");
    for(i=0; i<graph->n_nodes; i++) {
        printNode(graph->nodes[i], file, tree);
        // if (i % 10000 == 0) printf("%d\n", i);
    }
    fprintf(file, "}\n");
    fclose(file);
}