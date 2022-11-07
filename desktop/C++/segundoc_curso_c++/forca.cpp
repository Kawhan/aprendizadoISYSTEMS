#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include "nao_acertou.hpp"
#include "letra_existe.hpp"
#include "nao_enforcou.hpp"
#include "imprime_cabecalho.hpp"
#include "imprime_erros.hpp"
#include "imprime_palavra.hpp"
#include "chuta.hpp"
#include "adiciona_palavra.hpp"
#include "ler_arquivo.hpp"
#include "sorteia_palavra.hpp"
#include "imprime_final.hpp"
#include "salva_arquivo.hpp"

using namespace std;

string palavra_secreta;
map<char, bool> chutou;
vector<char> chutes_errados;


int main () {
    imprime_cabecalho();

    ler_arquivo();
    sorteia_palavra();

    while (nao_acertou() && nao_enforcou()) {
        imprime_erros();

        imprime_palavra();

        cout << endl;

        chuta();
    }

    imprime_final();
}