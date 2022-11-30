#include "contaCorrente.hpp"

ContaCorrente::ContaCorrente(std::string numeroConta, Titular titular): Conta(numeroConta, titular) {

}

float ContaCorrente::taxaDeSaque() const {
    return 0.05;
}