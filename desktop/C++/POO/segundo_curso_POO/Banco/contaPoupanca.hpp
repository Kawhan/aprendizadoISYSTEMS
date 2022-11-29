#pragma once 

#include "conta.hpp" 

class ContaPoupanca: public Conta {
    public:


    public:
        ContaPoupanca(std::string numeroConta, Titular titular);
        virtual void sacar (float valorASacar) override;
};