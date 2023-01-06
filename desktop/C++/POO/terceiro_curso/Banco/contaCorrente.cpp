#include "contaCorrente.hpp"

ContaCorrente::ContaCorrente(std::string numeroConta, Titular titular): Conta(numeroConta, titular) {

}

float ContaCorrente::taxaDeSaque() const {
    return 0.05;
}

void ContaCorrente::trasferePara(Conta& destino, float valor) {
    sacar(valor);
    destino.depositar(valor);
}

void ContaCorrente::operator+=(ContaCorrente& contaOrigem) {
    contaOrigem.trasferePara(*this, contaOrigem.recuperaSaldo()/2);
}