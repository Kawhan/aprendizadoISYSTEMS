#include <iostream>
#include <string>
#include "conta.hpp"

using namespace std;

int main() 
{
    Conta umaConta("123456", "Kawhan", "123.456.789.0");

    Conta umaConta2("23456", "teste", "000.000.000.0");
    

    umaConta.depositar(500);

    umaConta.sacar(200);


    cout << "Saldo da minha conta: " << umaConta.recuperaSaldo() << ". Saldo da outra conta: " << umaConta2.recuperaSaldo() << endl;
    return 0;
}