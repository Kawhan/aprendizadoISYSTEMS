from telefonesBr import TelefonesBr
import re

telefone = "55212648-1234"
# padrao = re.compile("([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([-]?)([0-9]{4})")
# resposta = re.findall(padrao, telefone)
# print(resposta)

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)