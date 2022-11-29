#pragma once
#include "titular.hpp"
#include <string>

class Conta
{
    private:
        static int numeroDeContas;
        std::string numeroConta;
        Titular titular;

        /* 1 = conta corrente e 2  = conta poupança */
    
    protected:
        float saldo;

    public:
        Conta(std::string numeroConta, Titular titular);
        virtual ~Conta();
        virtual void sacar(float valorASacar);
        void depositar(float valorADepositar);
        float recuperaSaldo() const;
        std::string recuperaNumeroConta() const;
        int recuperaNumeroContas() const;
};