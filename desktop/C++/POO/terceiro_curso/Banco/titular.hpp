#pragma once 
#include <string>
#include "pessoa.hpp"
#include "autenticavel.hpp"

class Titular:public Pessoa, public Autenticavel
{   
    public:
        Titular(CPF cpf, std::string nome, std::string senha);

};