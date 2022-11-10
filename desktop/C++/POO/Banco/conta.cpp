#include "conta.hpp"
#include <iostream>

// Conta::Conta(std::string numero, std::string nomeTitular, std::string cpfTutular)
// {
//     this-> numeroConta = numero;
//     this-> nomeTitular = nomeTitular;
//     this-> cpfTitular = cpfTitular;
//     this-> saldo = 0;
// }


Conta::Conta(std::string numeroConta, std::string nomeTitular, std::string cpfTitular): 
numeroConta(numeroConta), nomeTitular(nomeTitular),cpfTitular(cpfTitular),saldo(0)
{
}

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
std::string Conta::recuperaNumeroConta() const{
    return numeroConta;
}

std::string Conta::recuperaNomeTitular() const{
    return nomeTitular;
}

std::string Conta::recuperaCpfTitular() const{
    return cpfTitular;
}
