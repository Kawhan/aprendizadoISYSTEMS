#include "funcionario.hpp"

Funcionario::Funcionario(CPF cpf, std::string nome, float salario): Pessoa(cpf, nome), salario(salario){

}

std::string Funcionario::RecuperaNome() const{
    return nome;
}

float Funcionario::recuperaSalario() const {
    return salario;
}