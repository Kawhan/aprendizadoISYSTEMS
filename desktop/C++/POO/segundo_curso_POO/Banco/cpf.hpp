#pragma once
#include <string>

class CPF {
    private:
        std::string cpf;
    public:
        explicit CPF(std::string cpf);
        std::string getCPF() const;
};