import re
from statistics import quantiles

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    # Sanitização da URL
    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco. Ou string vazia"""
        if (type(url) == str):
            return url.strip()
        else:
            return ""
        
    # Validação da URL
    def valida_url(self):
        """Valida se a url está vazia"""
        if (not self.url):
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida.")
    
    # Separa base 
    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base
    
    
    # Separa os parametros
    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    # Busca o valor de um parametro
    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return f'A URL é {self.url} \nParâmetros: {self.get_url_parametros()}\nURL Base: {self.get_url_base()}'
    
    def __eq__(self, other):
        return self.url == other.url
    
    def __ne__(self, other):
        return self.url != other.url
        

extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real")
extrator_url2 = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
VALOR_DOLAR = 5.50
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
tipo_1_moeda = extrator_url.get_valor_parametro("moedaOrigem")
tipo_2_moeda = extrator_url.get_valor_parametro("moedaDestino")
print(valor_quantidade)
print(extrator_url)
print("O tamanho da URL:", len(extrator_url))
print(extrator_url == extrator_url2)

if (tipo_1_moeda == "real" and tipo_2_moeda == "dolar"):
    valor_conversao =  int(valor_quantidade) / VALOR_DOLAR
elif (tipo_1_moeda == "dolar" and tipo_2_moeda == "real"):
    valor_conversao = int(valor_quantidade) * VALOR_DOLAR
else:
    print("Valores não validos!")
    
print(valor_conversao)
