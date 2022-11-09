#pragma once
#include <string>

class Conta
{
    private:
        std::string numeroConta;
        std::string cpfTitular;
        std::string nomeTitular;

        float saldo = 0;

    public:
        void sacar(float valorASacar);
        void depositar(float valorADepositar);
        float recuperaSaldo() const;
        std::string recuperaNumeroConta();
        std::string recuperaCpfTitular();
        std::string recuperaNomeTitular();
        void definirNomeTitular(std::string nome);
        void definirNumeroConta(std::string numeroConta);
        void definirCpfTitular(std::string numeroCPF);
};