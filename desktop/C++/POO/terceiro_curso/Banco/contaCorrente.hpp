#pragma once

#include "conta.hpp"

class ContaCorrente final: public Conta 
{
    public:
        ContaCorrente(std::string numeroConta, Titular titular);
        float taxaDeSaque() const override;
        void trasferePara(Conta& destino, float valor);
        void operator+=(ContaCorrente& contaOrigem);
};