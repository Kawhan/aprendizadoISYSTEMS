#pragma once
#include <string>

class Conta
{
    private:
        std::string numeroConta;
        std::string cpfTitular;
        std::string nomeTitular;

        float saldo;

    public:
        Conta(std::string numeroConta, std::string nomeTitular, std::string cpfTitular);
        void sacar(float valorASacar);
        void depositar(float valorADepositar);
        float recuperaSaldo() const;
        std::string recuperaNumeroConta() const;
        std::string recuperaCpfTitular() const;
        std::string recuperaNomeTitular() const;
};