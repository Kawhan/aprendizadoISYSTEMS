#include <vector>
#include "ler_arquivo.hpp"
#include <ctime>
#include <cstdlib>

std::string sorteia_palavra() {
    std::vector<std::string> palavras = ler_arquivo();

    srand(time(0));
    int indice_sorteado = rand() % palavras.size();

    return palavras[indice_sorteado];
}