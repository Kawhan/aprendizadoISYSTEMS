#include <stdio.h>

void potencia(int number1, int number2) {
    int n = 1;
    

    for (int i=0; i < number2; i++) {
        n = n * number1;
    }

    printf("%d ^ %d = %d", number1, number2, n);
}

int main(void) {

    int numero = 4;
    int numero2 = 2;

    potencia(numero, numero2);
}