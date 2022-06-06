endereco = "Rua das flores 72, apartamento 1002, laranjeiras, Rio de Janeiro, RJ, 23440-120"

#RegEx
import re 

# 5 digitos + "-"(opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Math

if busca:
    cep = busca.group()
    print(cep)