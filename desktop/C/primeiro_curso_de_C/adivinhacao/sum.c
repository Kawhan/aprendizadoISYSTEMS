#include <stdio.h>

int main(void) {
    int limite = 100;
    int soma = 0;
    int number = 1;

    while(number <= limite) {
        soma += number;
        number++;
    }
    printf("Sua soma é: %d", soma);
}

