#include <iostream>
#include <string>
#include <map>
#include <array>
#include "nao_acertou.hpp"
#include "letra_existe.hpp"
#include "imprime_cabecalho.hpp"
#include "imprime_erros.hpp"
#include "imprime_palavra.hpp"
#include "chuta.hpp"
#include "adiciona_palavra.hpp"
#include "ler_arquivo.hpp"
#include "sorteia_palavra.hpp"
#include "salva_arquivo.hpp"

using namespace std;

static string palavra_secreta;
static map<char, bool> chutou;
static array<char, 5> chutes_errados;
static int chutes = 0;


int main () {
    imprime_cabecalho();

    palavra_secreta = sorteia_palavra();

    while (nao_acertou(palavra_secreta, chutou) && chutes < 5) {
        imprime_erros(chutes_errados);

        imprime_palavra(palavra_secreta, chutou);

        cout << endl;

        chuta(chutou, chutes_errados, palavra_secreta, chutes);
    }

    std::cout << "Fim de Jogo!" << std::endl;
    std::cout << "A palavra secreta era: " << palavra_secreta << std::endl;
    if(nao_acertou(palavra_secreta, chutou)) {
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