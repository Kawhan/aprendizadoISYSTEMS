#pragma once

#include "funcionario.hpp"
#include "autenticavel.hpp"
#include "diaDaSemana.hpp"
#include <string>

class Gerente: public Funcionario, public Autenticavel {
    public:
        Gerente(CPF cpf, std::string nome, float salario, DiaDaSemana diaDoPagamento, std::string senha);
        float bonificacao() const;
};