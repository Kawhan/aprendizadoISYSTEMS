#include <stdio.h>

int main(void) {

    // Imprime o cabeçalho do nosso jogo
    printf("*********************************************\n");
    printf("* Bem vindo ao nosso jogo de adivinhação *\n");
    printf("*********************************************\n");

    int numero_secreto = 42;
    int tentativas = 1;

    // printf("\nO número %d é o secreto. Não conta para ninguém!\n", numero_secreto);

    // Pedindo um chute ao usuário
    while (1) {
        int chute;

        printf("Tentativa %d\n", tentativas);

        printf("Qual é o seu chute? ");
        scanf("%d", &chute);
        printf("Seu chute foi %d\n", chute);

        if (chute < 0) {
            printf("Você não pode chuter números negativos!");

            continue;
        }

        int acertou = (numero_secreto == chute);
        int maior = chute > numero_secreto;

        if (acertou) {
            printf("\nParabéns! Você acertou!\n");
            printf("Jogue de novo, você é um bom jogador\n");
            
            break;
        }

        else if (maior) {
            printf("Seu chute foi maior que o número secreto\n");
        }

        else {
            printf("Seu chute foi menor que o número secreto\n");
        }

        tentativas++;
    }

    printf("Fim de jogo!\n");
    printf("Você acertou em %d tentativas!", tentativas);
}   