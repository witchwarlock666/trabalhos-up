#include "common.h"

void getMovies(Graph *graph, char *filename, Tree *tree) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Erro!");
        return;
    }
    char *buffer = malloc(sizeof(char) * 400);
    fgets(buffer, 105, file);

    int i = 0;
    char *imdbstr;
    int imdb;
    char *type;
    char *title;

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

        if (strcmp(type, "movie") == 0) {
            // printf("%s\n", title);
            insertNoGraph(tree, imdb, insertNode(graph, imdb, title));
            ++i;
            if (i % 100000 == 0) {
                printf("%d - %d\n", i, imdb);
            }
        }
    }
}