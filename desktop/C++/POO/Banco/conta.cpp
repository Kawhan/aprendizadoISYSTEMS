#include "conta.hpp"
#include <iostream>

void Conta::sacar (float valorASacar)
{
    if (valorASacar < 0 ) {
        std::cout << "Não pode sacar valor negativo" << std::endl;
        return;
    }

    if (valorASacar > saldo) {
        std::cout << "Saldo insuficiente" << std::endl;
        return;
    }

    saldo -= valorASacar;
}

void Conta::depositar (float valorADepositar)
{
    if (valorADepositar < 0 ) {
        std::cout << "Não pode depositar valor negativo" << std::endl;
        return;
    }
    saldo += valorADepositar;
}

float Conta::recuperaSaldo() const{
    return saldo;
}


// Getters
std::string Conta::recuperaNumeroConta() {
    return numeroConta;
}

std::string Conta::recuperaNomeTitular() {
    return nomeTitular;
}

std::string Conta::recuperaCpfTitular() {
    return cpfTitular;
}


// Setters
void Conta::definirNomeTitular(std::string nome){
    nomeTitular = nome;
}

void Conta::definirNomeTitular(std::string numeroConta) {
    numeroConta = numeroConta;
}

void Conta::definirCpfTitular(std::string numeroCPF) {
    cpfTitular = numeroCPF;
}