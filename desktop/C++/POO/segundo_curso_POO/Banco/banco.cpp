#include <iostream>
#include <string>
#include "conta.hpp"
#include "titular.hpp"
#include "cpf.hpp"
#include "funcionario.hpp"
#include "contaPoupanca.hpp"
#include "contaCorrente.hpp"
#include "autenticavel.hpp"

using namespace std;

void RealizaSaque(Conta& conta) {
    conta.sacar(200);
}

void Fazlogin(Autenticavel& alguem, string senha) {
    if (alguem.autentica(senha)) {
        cout << "login Realizado com sucesso" << endl;
    } else {
        cout << "Senha inválida" << endl;
    }
}

int main() 
{
    Titular titular (CPF("123.456.789.0") , "Kawhann", "umaSenha");
    ContaPoupanca umaConta("123456", titular);

    umaConta.depositar(500);

    RealizaSaque(umaConta);

    cout << umaConta.recuperaSaldo() << endl;

    

    Titular titular2 (CPF("000.000.000.0") , "testee", "umaSenha");
    ContaCorrente umaConta2("23456", titular2);

    umaConta2.depositar(500);
    RealizaSaque(umaConta2);

    Titular titular3 (CPF("000.000.000.0") , "testeee", "umaSenha");
    ContaCorrente umaConta3("23456", titular3);

    umaConta3.depositar(500);

    umaConta2.trasferePara(umaConta3, 250);

  

    cout << "Saldo da minha conta: " << umaConta.recuperaSaldo() << ". Saldo da outra conta: " << umaConta2.recuperaSaldo() << endl;

    cout << "Número de contas: " << umaConta.recuperaNumeroContas() << endl;
    return 0;
}