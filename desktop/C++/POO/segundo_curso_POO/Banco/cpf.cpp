#include "cpf.hpp"

CPF::CPF(std::string cpf): cpf(cpf) {

}

std::string CPF::getCPF() const{
    return cpf;
}