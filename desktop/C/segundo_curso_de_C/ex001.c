#include <stdio.h>

int main(void) {
    int notas[5];
    notas[0] = 1;
    notas[1] = 4;
    notas[2] = 7;
    notas[3] = 5;
    notas[4] = 10;

    for (int i = 0; i<5; i++) {
        printf("%d\n", notas[i]);
    }
}