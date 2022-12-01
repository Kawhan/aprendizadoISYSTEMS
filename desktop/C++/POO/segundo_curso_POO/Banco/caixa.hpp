#pragma once

#include "funcionario.hpp"

class Caixa: public Funcionario {
    public:
        Caixa(CPF cpf, std::string nome, float salario);
        float bonificacao() const;
};