#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {

    printf("\n\n");
    printf("         P  /_\\  P                             \n");                     
    printf("        /_\\_|_|_/_\\                           \n");
    printf("    n_n | ||. .|| | n_n         Bem vindo ao    \n");
    printf("    |_|_|nnnn nnnn|_|_|     Jogo de Adivinhação!\n");
    printf("   |" "  |  |_|  |"  " |                        \n");
    printf("   |_____| ' _ ' |_____|                        \n");
    printf("         \\__|_|__/                             \n\n\n");

    int segundos = time(0);

    srand(segundos);

    int numero_secreto = rand() % 100;
    int tentativas = 1;

    int acertou = 0;

    int nivel;
    printf("Qual o nível de dificuldade? \n");
    printf("(1) Fácil (2) Médio (3) Dificil\n\n");
    printf("Escolha: ");
    scanf("%d", &nivel);

    int numero_tentativas;
    
    switch(nivel) {
        case 1:
            numero_tentativas = 20;
            break;
        case 2:
            numero_tentativas = 15;
            break;
        default:
            numero_tentativas = 6;
            break;
    }

    double pontos = 1000; 

    // printf("\nO número %d é o secreto. Não conta para ninguém!\n", numero_secreto);

    // Pedindo um chute ao usuário
    for (int i = 1; i <= numero_tentativas; i++) {
        int chute;

        printf("Tentativa %d\n", i);

        printf("Qual é o seu chute? ");
        scanf("%d", &chute);
        printf("Seu chute foi %d\n", chute);

        if (chute < 0) {
            printf("Você não pode chuter números negativos!");

            continue;
        }

        acertou = (numero_secreto == chute);
        int maior = chute > numero_secreto;

        if (acertou) {
            break;
        }

        else if (maior) {
            printf("Seu chute foi maior que o número secreto\n");
        }

        else {
            printf("Seu chute foi menor que o número secreto\n");
        }

        tentativas++;

        double pontosperdidos = (abs)(chute - numero_secreto) / (double)2;
        pontos  = pontos - pontosperdidos;
    }

    printf("Fim de jogo!\n");

    if (acertou) {

        printf("\n\n\n");
        printf("                   OOOOOOOOOOO                   \n");
        printf("                OOOOOOOOOOOOOOOOOOO              \n"); 
        printf("              OOOOOO  OOOOOOOOO  OOOOOO          \n");
        printf("           OOOOOO      OOOOO      OOOOOO         \n");
        printf("         OOOOOOOO  #   OOOOO  #   OOOOOOOO       \n");
        printf("        OOOOOOOOOO    OOOOOOO    OOOOOOOOOO      \n");
        printf("        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    \n");
        printf("        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    \n");
        printf("        OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO    \n");
        printf("         OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO     \n");
        printf("         OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO       \n");
        printf("           OOOOO   OOOOOOOOOOOOOOO   OOOO        \n");
        printf("            OOOOOO   OOOOOOOOO   OOOOOO          \n");
        printf("              OOOOOO         OOOOOO              \n");
        printf("                    OOOOOOOOOOOO                 \n\n\n");

        printf("Você ganhou!\n");
        printf("Você acertou em %d tentativas!\n", tentativas);
        printf("Total de pontos %.1f\n", pontos);  
    } else {        
        printf("Você perdeu tente novamente!\n");

        printf("       \\|/ ____ \\|/    \n");
        printf("        @~/ ,. \\~@      \n");
        printf("       /_( \\__/ )_\\    \n");
        printf("          \\__U_/        \n");
    }

   
}   