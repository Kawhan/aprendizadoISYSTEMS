#include "gerente.hpp"

Gerente::Gerente(CPF cpf, std::string nome, float salario, std::string senha): Funcionario(cpf, nome, salario), Autenticavel(senha) {
    
}

float Gerente::bonificacao() const {
    return recuperaSalario() * 0.5;
}