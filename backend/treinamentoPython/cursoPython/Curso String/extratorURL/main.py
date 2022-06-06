#url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = "        "

# Sanitização da URL
url = url.strip(" ", "")


# Validação da URL
if (url == ""):
    raise ValueError("A URL está vazia")

# Separa base e os parametros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)

# Busca o valor de um parametro

# Se eu tirar o ultimo indice que restringe o final e deixar sem nada ele percorre até o final
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Posso passar string para o find e ele vai me retornar o indice de começo se essa string tiver lá
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)


# Pegando o tamanho do parametro
tamanho_parametro = len(parametro_busca)

# Pega o indice inicial da nossa String procurada e soma com tamanho do parametro +1 para ir até o "=" da url
indice_valor = indice_parametro + tamanho_parametro + 1

# Procura o indice do "&" para que possa ir até ele no caso de que seja o primeiro parametro
# o segundo argumento é procure apartir de...
indice_e_comercial = url_parametros.find("&", indice_valor)

# Verificando se encontrou o & depois do "=" e a string
# Se ele não encontrou ele retorna -1 e ai vamos fatiar até o final
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)