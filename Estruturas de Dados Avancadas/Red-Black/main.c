#include "tree.c"

int main() {

    struct no **root = init_tree(14);

    int n = 7;
    int a[7] = { 7, 6, 5, 4, 3, 2, 1 };

    for (int i = 0; i < n; i++) {
        create(root, a[i]);
    }

    print_tree(*root);

    free_tree(*root);

    return 0;
}