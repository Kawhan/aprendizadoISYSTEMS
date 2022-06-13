'''
Como o método __iter__() serve para retornar um iterador e nossa classe será, de fato, um iterador, 
faremos com que ele retorne o próprio objeto. 

No caso do método __next()__, implementaremos o código que devolverá uma linha que queremos por vez:
'''


class IteradorHttp():
    def __init__(self):
        self.registro = open('links.txt', 'r')
        self.linha_atual = ''
    def __iter__(self):
        return self
    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration

iterador = IteradorHttp()

for url in iterador:
    print(url)