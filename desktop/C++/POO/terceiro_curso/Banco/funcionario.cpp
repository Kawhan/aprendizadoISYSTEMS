#include "funcionario.hpp"

Funcionario::Funcionario(CPF cpf, std::string nome, float salario, DiaDaSemana diaDoPagamento): 
Pessoa(cpf, nome), salario(salario), diaDoPagamento(diaDoPagamento){

}

std::string Funcionario::RecuperaNome() const{
    return nome;
}

float Funcionario::recuperaSalario() const {
    return salario;
}