#pragma once
#include "titular.hpp"
#include <string>

class Conta
{
    private:
        static int numeroDeContas;
        std::string numeroConta;
        Titular titular;

        float saldo;

    public:
        Conta(std::string numeroConta, Titular titular);
        ~Conta();
        void sacar(float valorASacar);
        void depositar(float valorADepositar);
        float recuperaSaldo() const;
        std::string recuperaNumeroConta() const;
        int recuperaNumeroContas() const;
};