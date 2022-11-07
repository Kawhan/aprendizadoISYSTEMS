#include <iostream>
#include "letra_existe.hpp"
#include <map>
#include <vector>

extern std::map<char, bool> chutou;
extern std::vector<char> chutes_errados;

void chuta() {
    std::cout << "Seu chute: ";
    char chute;
    std::cin >> chute;

    chutou[chute] = true;

    
    if (letra_existe(chute)) {
        std::cout << "Você acertou! Seu chute está na palavra." << std::endl;
    }
    else {
        std::cout << "Você errou! Seu chute não está na palavra." << std::endl;
        chutes_errados.push_back(chute);
    }
    std::cout << std::endl;
}