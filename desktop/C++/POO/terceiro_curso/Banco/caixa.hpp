#pragma once

#include "funcionario.hpp"
#include "diaDaSemana.hpp"


class Caixa: public Funcionario {
    public:
        Caixa(CPF cpf, std::string nome, float salario, DiaDaSemana diaDoPagamento);
        float bonificacao() const;
};