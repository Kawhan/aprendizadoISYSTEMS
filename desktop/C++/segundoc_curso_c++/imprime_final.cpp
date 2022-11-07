#include <iostream>
#include <string>
#include "nao_acertou.hpp"
#include "adiciona_palavra.hpp"

extern std::string palavra_secreta;


void imprime_final() {
    std::cout << "Fim de Jogo!" << std::endl;
    std::cout << "A palavra secreta era: " << palavra_secreta << std::endl;
    if(nao_acertou()) {
        std::cout << "Você perdeu! Tente novamente!" << std::endl;
    } 
    else {
        std::cout << "Parabéns! Você acertou a palavra secreta!" << std::endl;

        std::cout << "Você deseja adicionar uma nova palavra ao banco? (S/N)";
        char resposta;
        std::cin >> resposta;

        if (resposta == 'S') {
            adiciona_palavra();
        }
    }
}