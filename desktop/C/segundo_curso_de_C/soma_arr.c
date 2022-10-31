#include <stdio.h>

void sum(int numeros[10]) {
    int sum_arr = 0;
    for (int i = 0; i < 10; i++) {
        sum_arr += numeros[i];
    }

    printf("%d", sum_arr);
}

int main() {
    int numeros[10];

    numeros[0] = 10;
    numeros[1] = 10;
    numeros[2] = 10;
    numeros[3] = 10;
    numeros[4] = 10;
    numeros[5] = 10;
    numeros[6] = 10;
    numeros[7] = 10;
    numeros[8] = 10;
    numeros[9] = 10;

    sum(numeros);
}