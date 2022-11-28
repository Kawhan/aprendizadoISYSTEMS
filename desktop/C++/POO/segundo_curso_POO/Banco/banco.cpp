#include <iostream>
#include <string>
#include "conta.hpp"
#include "titular.hpp"
#include "cpf.hpp"
#include "funcionario.hpp"

using namespace std;

int main() 
{
    Titular titular (CPF("123.456.789.0") , "Kawhann");
    Conta umaConta("123456", titular);

    umaConta.depositar(500);

    umaConta.sacar(200);

    Titular titular2 (CPF("000.000.000.0") , "testee");
    Conta umaConta2("23456", titular2);

    umaConta2.depositar(500);

    Titular titular3 (CPF("000.000.000.0") , "testeee");
    Conta umaConta3("23456", titular3);

    umaConta3.depositar(500);

  

    cout << "Saldo da minha conta: " << umaConta.recuperaSaldo() << ". Saldo da outra conta: " << umaConta2.recuperaSaldo() << endl;

    cout << "Número de contas: " << umaConta.recuperaNumeroContas() << endl;

    Funcionario funcionario(CPF("123-456-789"), "Kawhan", 3000.00);
    return 0;
}