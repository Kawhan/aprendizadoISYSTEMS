#pragma once 
#include <string>
#include "cpf.hpp"

class Titular {
    private:
        CPF cpf;
        std::string nome;

    public:
        Titular(CPF cpf, std::string nome);
        std::string recuperaNomeTitular() const;
    private:
        void verificaTamanhoDoNome() const;
};