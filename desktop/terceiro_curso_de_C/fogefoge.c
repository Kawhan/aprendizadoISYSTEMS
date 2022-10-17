#include <stdio.h>
#include <stdlib.h>
#include "fogefoge.h"

char** mapa;
int linhas;
int colunas;

void libera_mapa() {
    for (int i = 0; i < linhas; i++) {
        free(mapa[i]);
    }
    free(mapa);
}

void aloca_mapa() {
    mapa = malloc(sizeof(char*) * linhas);
    for (int i = 0; i < linhas; i++) {
        mapa[i] = malloc(sizeof(char)  * (colunas + 1));
    }
}

void lermapa() {
    //     linhas | Colunas
    
    FILE *f;
    f = fopen("mapa.txt", "r");
    if (f == 0) {
        printf("Erro na leitura do mapa\n");
        exit(1);
    }
    
    fscanf(f, "%d %d", &linhas, &colunas);
    // printf("Linhas %d colunas %d\n", linhas, colunas);

    ///////////////////////
    aloca_mapa();

    // int** v = malloc(sizeof(int*) * 5);  
    // for (int i = 0; i < 5; i++) {
    //     v[i] = malloc(sizeof(int) * 10);
    // }

    // *v = 10;
    // printf("inteiro alocado %d\n", *v);

    // for (int i = 0; i < 5; i++) {
    //     free(v[i]);
    // }
    // free(v);

    //////////////////////


    for (int i = 0; i < 5; i++) {
        fscanf(f, "%s", mapa[i]);
    }
    
    fclose(f);
}

int main() {

    lermapa();
    

    for (int i = 0; i < 5; i++) {
        printf("%s\n", mapa[i]);
    }


    libera_mapa();
}