#include <stdio.h>

int main(void) {

    // Imprime o cabeçalho do nosso jogo
    printf("*********************************************\n");
    printf("* Bem vindo ao nosso jogo de adivinhação *\n");
    printf("*********************************************\n");

    int numero_secreto = 42;

    // printf("\nO número %d é o secreto. Não conta para ninguém!\n", numero_secreto);

    // Pedindo um chute ao usuário
    for (int tentativa=1; tentativa <= 3; tentativa++) {
        int chute;

        printf("Tentativa %d de 3\n", tentativa);

        printf("Qual é o seu chute? ");
        scanf("%d", &chute);
        printf("Seu chute foi %d\n", chute);
        int acertou = (numero_secreto == chute);

        if (acertou) {
            printf("\nParabéns! Você acertou!\n");
            printf("Jogue de novo, você é um bom jogador\n");
            break;
        }
        else {
            if (chute > numero_secreto) {
                printf("Seu chute foi maior que o número secreto\n");
            }
            if (chute < numero_secreto) {
                printf("Seu chute foi menor que o número secreto\n");
            }
        }
    }
}   