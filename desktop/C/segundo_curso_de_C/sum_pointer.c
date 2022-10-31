#include <stdio.h>

void sum(int a, int b, int* sum) {
    (*sum) = a + b;
}

int main() {

    int num = 0;
    int a = 3;
    int b = 4;

    sum(a, b, &num);
    printf("%d",num);
}