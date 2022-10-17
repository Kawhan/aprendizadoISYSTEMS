#include <stdio.h>
#include <stdlib.h>

int main() {
    int numeros[20][10];

    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%c",numeros[i][j]);
        }
        printf("\n");
    }
}