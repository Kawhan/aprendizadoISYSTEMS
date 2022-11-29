#include "conta.hpp"
#include "titular.hpp"
#include <iostream>

// Conta::Conta(std::string numero, std::string nomeTitular, std::string cpfTutular)
// {
//     this-> numeroConta = numero;
//     this-> nomeTitular = nomeTitular;
//     this-> cpfTitular = cpfTitular;
//     this-> saldo = 0;
// }

int Conta::numeroDeContas = 0;

Conta::Conta(std::string numeroConta, Titular titular): 
numeroConta(numeroConta), titular(titular) ,saldo(0)
{
    
    numeroDeContas++;
}

Conta::~Conta() {
    numeroDeContas--;
}


void Conta::sacar (float valorASacar)
{
    if (valorASacar < 0 ) {
        std::cout << "Não pode sacar valor negativo" << std::endl;
        return;
    }

    float tarifaDeSaque = valorASacar * 0.05;
    float valorDoSaque = valorASacar + tarifaDeSaque;

    if (valorDoSaque > saldo) {
        std::cout << "Saldo insuficiente" << std::endl;
        return;
    }

    saldo -= valorDoSaque;
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
std::string Conta::recuperaNumeroConta() const{
    return numeroConta;
}

int Conta::recuperaNumeroContas() const {
    return numeroDeContas;
}

