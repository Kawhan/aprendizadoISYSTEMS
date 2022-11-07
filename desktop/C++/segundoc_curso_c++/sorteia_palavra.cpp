#include <vector>
#include <iostream>
#include <string>
#include "ler_arquivo.hpp"
#include <ctime>
#include <cstdlib>

extern std::string palavra_secreta;

void sorteia_palavra() {
    std::vector<std::string> palavras = ler_arquivo();

    srand(time(0));
    int indice_sorteado = rand() % palavras.size();

    palavra_secreta = palavras[indice_sorteado];
}