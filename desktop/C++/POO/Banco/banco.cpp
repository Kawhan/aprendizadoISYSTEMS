#include <iostream>
#include <string>
#include "conta.hpp"

using namespace std;

int main() 
{
    Conta umaConta;
    umaConta.definirNomeTitular("Kawhan");

    Conta umaConta2;
    

    umaConta.depositar(500);

    umaConta.sacar(200);


    cout << "Saldo da minha conta: " << umaConta.recuperaSaldo() << ". Saldo da outra conta: " << umaConta2.recuperaSaldo() << endl;
    return 0;
}