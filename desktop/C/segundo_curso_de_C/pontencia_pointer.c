#include <stdio.h>

void potencia(int number1, int number2, int* resultado) {
    (*resultado) = 1;
    

    for (int i=0; i < number2; i++) {
        (*resultado) = (*resultado) * number1;
    }
}

int main(void) {

    int numero = 4;
    int numero2 = 2;
    int resultado;

    potencia(numero, numero2, &resultado);
    printf("%d",resultado);
}