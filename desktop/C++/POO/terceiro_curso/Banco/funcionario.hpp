#pragma once
#include "pessoa.hpp"
#include "diaDaSemana.hpp"
#include <string>

class Funcionario: public Pessoa
{
    private:
        float salario;

        // 0 = Domingo, 1 = Segunda, etc
        DiaDaSemana diaDoPagamento;

    public:
        Funcionario(CPF cpf, std::string nome, float salario, DiaDaSemana diaDoPagamento);
        std::string RecuperaNome() const;
        virtual float bonificacao() const = 0;
        float recuperaSalario() const;
};