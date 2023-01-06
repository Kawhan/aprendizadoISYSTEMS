#include "contaPoupanca.hpp"
#include <iostream>

ContaPoupanca::ContaPoupanca(std::string numeroConta, Titular titular):Conta(numeroConta, titular) {

}

float ContaPoupanca::taxaDeSaque() const {
    return 0.03;
}