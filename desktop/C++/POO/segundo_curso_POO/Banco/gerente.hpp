#pragma once

#include "funcionario.hpp"
#include "autenticavel.hpp"
#include <string>

class Gerente: public Funcionario, public Autenticavel {
    public:
        Gerente(CPF cpf, std::string nome, float salario, std::string senha);
        float bonificacao() const;
};