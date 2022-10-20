#include <stdio.h>

int fibonaci(int numero) {
    if (numero == 0) {
        return 0;
    }
    if (numero == 1) {
        return 1;
    }

    return fibonaci(numero-1) + fibonaci(numero-2);
}

int main() {
    fibonaci(3);
}