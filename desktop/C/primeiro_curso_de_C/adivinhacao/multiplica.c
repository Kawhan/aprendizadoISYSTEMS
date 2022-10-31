#include <stdio.h>

int main(void) {
    int valor1;
    int valor2;

    printf("Digite seu valor 1: ");
    scanf("%d", &valor1);

    printf("Digite seu valor 2: ");
    scanf("%d", &valor2);

    int mult = valor1 * valor2;
    printf("A multiplicação do valor1 (%d) e o valor2 (%d) é: %d", valor1, valor2, mult);
}