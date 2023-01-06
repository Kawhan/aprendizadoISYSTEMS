#pragma once
#include "cpf.hpp"
#include <string>

class Pessoa
{
    protected:
        CPF cpf;
        std::string nome;
    public:
        Pessoa(CPF cpf, std::string nome);
        std::string recuperaNomePessoa() const;
    private:
        void verificaTamanhoDoNome() const;
};