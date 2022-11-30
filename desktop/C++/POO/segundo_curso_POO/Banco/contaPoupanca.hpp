#pragma once 

#include "conta.hpp" 

class ContaPoupanca final: public Conta {
    public:


    public:
        ContaPoupanca(std::string numeroConta, Titular titular);
        float taxaDeSaque() const override;
};