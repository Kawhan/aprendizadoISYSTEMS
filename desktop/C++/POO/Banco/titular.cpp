#include "titular.hpp"
#include "cpf.hpp"
#include <iostream>

Titular::Titular(CPF cpf, std::string nome): cpf(cpf), nome(nome) 
{
    verificaTamanhoDoNome();
}


void Titular::verificaTamanhoDoNome() const{
    if (nome.size() < 5 )  {
        std::cout << "Nome muito curto" << std::endl;
        exit(1);
    }
}

std::string Titular::recuperaNomeTitular() const{
    return nome;
}

