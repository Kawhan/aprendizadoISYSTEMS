#include <iostream>
#include <fstream>
#include "salva_arquivo.hpp"


void salva_arquivo(std::vector<std::string> lista_palavras) {
    std::ofstream arquivo;

    arquivo.open("palavras.txt");

    if (arquivo.is_open()) {
        arquivo << lista_palavras.size() << std::endl;

        for (std::string palavra : lista_palavras) {
            arquivo << palavra << std::endl;
        }

        arquivo.close();
    }
    else {
        std::cout << "Não foi possível acessar o banco de palavras." << std::endl;
        exit(0);
    }

    
}
