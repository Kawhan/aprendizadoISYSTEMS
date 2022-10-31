#include <stdio.h>

int main(void) {
    int numero;

    printf("Por favor digite um número inteiro: ");

    scanf("%d", &numero);

    if (numero < 0) {
        printf("Número menor que zero! Por favor tentar novamente.");
    } else {
        for (int number=0; number <= 10; number++) {
            printf("%d x %d = %d\n", numero, number, numero * number);
        }
    }

}