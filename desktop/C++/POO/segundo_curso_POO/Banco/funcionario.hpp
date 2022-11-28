#pragma once
#include "pessoa.hpp"
#include <string>

class Funcionario: public Pessoa
{
    private:
        float salario;
    public:
        Funcionario(CPF cpf, std::string nome, float salario);
        std::string RecuperaNome();
};