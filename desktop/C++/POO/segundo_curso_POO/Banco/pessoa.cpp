#include <iostream>
#include "pessoa.hpp"

Pessoa::Pessoa(CPF cpf, std::string nome):cpf(cpf), nome(nome) {

}

void Pessoa::verificaTamanhoDoNome() const{
    if (nome.size() < 5 )  {
        std::cout << "Nome muito curto" << std::endl;
        exit(1);
    }
}


std::string Pessoa::recuperaNomePessoa() const{
    return nome;
}