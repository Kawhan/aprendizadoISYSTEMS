#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int numbers[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

void verificanumero(char number)
{
    if (number == '0')
    {
        numbers[0]++;
    }
    else if (number == '1')
    {
        numbers[1]++;
    }
    else if (number == '2')
    {
        numbers[2]++;
    }
    else if (number == '3')
    {
        numbers[3]++;
    }
    else if (number == '4')
    {
        numbers[4]++;
    }
    else if (number == '5')
    {
        numbers[5]++;
    }
    else if (number == '6')
    {
        numbers[6]++;
    }
    else if (number == '7')
    {
        numbers[7]++;
    }
    else if (number == '8')
    {
        numbers[8]++;
    }
    else if (number == '9')
    {
        numbers[9]++;
    }
}

void imprimenumero() {
    printf("%d %d %d %d %d %d %d %d %d %d", numbers[0], numbers[1], numbers[2],
           numbers[3], numbers[4], numbers[5], numbers[6], numbers[7], numbers[8], numbers[9]);
}

int main(int argc, char **argv)
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        char c = argv[1][i];
        verificanumero(c);
    }
    
    imprimenumero();

    return 0;
}
