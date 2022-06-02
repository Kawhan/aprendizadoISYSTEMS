class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()
    
    def dar_like(self):
        self._likes += 1
    
    def __str__(self):
        return f'{self._nome} - {self.ano}: {self._likes} Likes' 
        

class Filme(Programa):
    def __init__(self,nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano}- {self.duracao} minutos -  {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano}- {self.temporadas} temporadas -  {self._likes} Likes'

# Posso fazer com que ela herde o comportamento de uma lista
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome 
        self._programas = programas
    
    # Esse metodo deixa o objeto com comportamento de lista de forma iteravel
    # Ganha o for in e o in
    # Fora que eu posso mostrar os elementos em posições na minha lista
    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas
    
    # colocar o data model de sequencia para mostra o tamanho com len 
    def __len__(self):
        return len(self._programas)
    
  


vingadores = Filme('vingadores - guerra infinita', 2018, 160) 
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor  = Serie('Demolidor', 2016, 2)


vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.nome = "the boys"

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')
# Colocando o polimorfismo em pratica, como todos fazem parte de uma unica super classe não importa as subclasses que eles tem
# Eles podem interar também de forma mais tranquila sem muitos ifs por causa da questão que cada um tem um método imprime
for programa in playlist_fim_de_semana:
    print(programa)


print(demolidor in playlist_fim_de_semana)