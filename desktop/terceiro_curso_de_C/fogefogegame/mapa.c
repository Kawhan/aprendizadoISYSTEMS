#include "mapa.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void copiamapa(MAPA* destino, MAPA* origem) {
    destino->linhas = origem->linhas;
    destino->colunas = origem->colunas;

    aloca_mapa(destino);
    for (int i = 0; i < origem->linhas; i++) {
        strcpy(destino->matriz[i], origem->matriz[i]);
    }
}

void andando_mapa(MAPA* m, int xorigem, int yorigem, int xdestino, int ydestino) {
    char personagem = m->matriz[xorigem][yorigem];

    m->matriz[xdestino][ydestino] = personagem;
    m->matriz[xorigem][yorigem] = VAZIO;
}

int podeandar(MAPA* m, char personagem , int x, int y) {
    return ehvalida(m, x , y) && !ehparede(m, x, y) && !ehpersonagem(m, personagem, x, y);
}

int ehpersonagem(MAPA* m, char personagem, int x, int y) {
    return m->matriz[x][y] == personagem;
}

int encontra_mapa(MAPA* m, POSICAO* p, char c) {
     for (int i = 0; i < m->linhas; i++) {
        for (int j = 0; j < m->colunas; j++) {
            if(m->matriz[i][j] == c) {
                p->x = i;
                p->y = j;
                return 1;
            }
        }
    }

    return 0;
}

int ehparede(MAPA* m, int x, int y) {
	return 
		m->matriz[x][y] == PAREDE_VERTICAL ||
		m->matriz[x][y] == PAREDE_HORIZONTAL;
}

int ehvalida(MAPA* m, int x, int y) {
    if (x >= m->linhas) {
        return 0;
    }

    if (y >= m->colunas) {
        return 0;
    }


    return 1;
}

int ehvazia(MAPA* m, int x, int y) {
    return m->matriz[x][y] == VAZIO;
}

void libera_mapa(MAPA* m) {
    for (int i = 0; i < m->linhas; i++) {
        free(m->matriz[i]);
    }
    free(m->matriz);
}

void aloca_mapa(MAPA* m) {
    m->matriz = malloc(sizeof(char*) * m->linhas);
    for (int i = 0; i < m->linhas; i++) {
        m->matriz[i] = malloc(sizeof(char)  * (m->colunas + 1));
    }
}

void lermapa(MAPA* m) {
    //     linhas | Colunas
    
    FILE *f;
    f = fopen("mapa.txt", "r");
    if (f == 0) {
        printf("Erro na leitura do mapa\n");
        exit(1);
    }
    
    fscanf(f, "%d %d", &(m->linhas), &(m->colunas));
    // printf("Linhas %d colunas %d\n", linhas, colunas);

    ///////////////////////
    aloca_mapa(m);

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
        fscanf(f, "%s", m->matriz[i]);
    }
    
    fclose(f);
}

