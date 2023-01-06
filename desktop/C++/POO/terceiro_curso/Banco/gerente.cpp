#include "gerente.hpp"

Gerente::Gerente(CPF cpf, std::string nome, float salario, DiaDaSemana diaDoPagamento, std::string senha): 
Funcionario(cpf, nome, salario, diaDoPagamento), Autenticavel(senha) {
    
}

float Gerente::bonificacao() const {
    return recuperaSalario() * 0.5;
}