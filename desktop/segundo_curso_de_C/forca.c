#include <stdio.h>
#include <string.h>

void abertura()
{
    printf("***********************\n");
    printf("*    Jogo de Forca    *\n");
    printf("***********************\n\n");
}

void chuta(char chutes[26], int *tentativas)
{
    char chute;
    scanf(" %c", &chute);

    chutes[(*tentativas)] = chute;
    (*tentativas)++;
}

int ja_chutou(char letra, char chutes[26], int tentativas)
{
    int achou = 0;

    for (int j = 0; j < tentativas; j++)
    {
        if (chutes[j] == letra)
        {
            achou = 1;
            break;
        }
    }

    return achou;
}

int main()
{
    char palavrasecreta[20];

    sprintf(palavrasecreta, "Melancia");

    int acertou = 0;
    int enforcou = 0;

    char chutes[26];
    int tentativas = 0;

    // Abertura
    abertura();

    do
    {
        // Começar nosso jogo

        // Imprime a palavra secreta
        for (int i = 0; i < strlen(palavrasecreta); i++)
        {

            // chutando uma letra
            int achou = ja_chutou(palavrasecreta[i], chutes, tentativas);

            if (achou)
            {
                printf("%c ", palavrasecreta[i]);
            }
            else
            {
                printf("_ ");
            }
        }
        printf("\n");

        // Captura novo chute
        chuta(chutes, &tentativas);

    } while (!acertou && !enforcou);
}