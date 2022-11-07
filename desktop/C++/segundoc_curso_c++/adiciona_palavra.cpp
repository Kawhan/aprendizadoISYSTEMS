#include <iostream>
#include <string>
#include <vector>
#include "ler_arquivo.hpp"
#include "salva_arquivo.hpp"

void adiciona_palavra () {
    std::cout << "Digite a nova palavra, usando letras maiúsculas." << std::endl;

    std::string nova_palavra;
    std::cin >> nova_palavra;

    std::vector<std::string> lista_palavra = ler_arquivo();
    lista_palavra.push_back(nova_palavra);

    salva_arquivo(lista_palavra);
}