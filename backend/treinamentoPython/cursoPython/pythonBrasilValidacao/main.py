from datetime import datetime, timedelta
from datas_br import DatasBr
from acesso_cep import BuscaEndereco
import requests

# Essa primeira classe retorna para gente uma hora exata que estamos compilando nosso código

# Time delta serve para fazer somas em tempo a uma data

# hoje =  DatasBr()

# print(hoje.tempo_cadastro())

cep ="01001000"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro)
print(cidade)
print(uf)
# print(a)
# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# 200 é bom
# print(r.text)