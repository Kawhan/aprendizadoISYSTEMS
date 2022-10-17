#include <stdlib.h>
#include <stdio.h>

int main() {
    int linhas = 5;
    int colunas = 10;

    int** v = malloc(sizeof(int*) * linhas);
    for (int i = 0; i < linhas; i++) {
        v = malloc(sizeof(int) * (colunas + 1));
    }

    for (int i = 0; i < linhas; i++) {
        free(v[i]);
    }

    free(v);
}