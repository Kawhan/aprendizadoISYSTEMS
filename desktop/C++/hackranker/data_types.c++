#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int number;
    long value;
    char ch;
    float number_float;
    double number_double;
    scanf("%d %ld %c %f %lf", &number, &value, &ch, &number_float, &number_double);
    
    printf("%d\n%ld\n%c\n%f\n%lf", number, value, ch, number_float, number_double);
    return 0;
}
