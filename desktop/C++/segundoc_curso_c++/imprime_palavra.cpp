#include <iostream>
#include "imprime_palavra.hpp"

void imprime_palavra(std::string& palavra_secreta, const std::map<char, bool>& chutou) {
    for (char letra : palavra_secreta) 
        {
            if (chutou.find(letra) == chutou.end() || !chutou.at(letra)) 
            {
                std::cout << "_ ";
            }
            else {
                std::cout << letra << " ";
            }
        }
}