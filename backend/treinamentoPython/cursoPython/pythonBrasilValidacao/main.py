from datetime import datetime, timedelta
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

# Essa primeira classe retorna para gente uma hora exata que estamos compilando nosso código

# Time delta serve para fazer somas em tempo a uma data

# hoje =  DatasBr()

# print(hoje.tempo_cadastro())

cep = 58780000
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

