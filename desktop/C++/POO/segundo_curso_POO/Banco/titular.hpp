#pragma once 
#include <string>
#include "pessoa.hpp"

class Titular:public Pessoa 
{   
    public:
        Titular(CPF cpf, std::string nome);

};