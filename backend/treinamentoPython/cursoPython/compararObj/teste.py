# __eq__(), chamado pelo operador ==
# __ne__(), chamado pelo operador !=
# __gt__(), chamado pelo operador >
# __lt__(), chamado pelo operador <
# __ge__(), chamado pelo operador >=
# __le__(), chamado pelo operador <=


class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    def __str__(self):
        return self.titulo + ' - ' + self.diretor
    
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo
    
    def __ne__(self, outro_filme):
        return self.titulo != outro_filme.titulo


def pega_todos_os_filmes():
    ## implementação da função
    filme_1 = Filme('A Teoria de Tudo', 'James Marsh')
    filme_2 = Filme('La La Land', 'Damien Chazelle')
    filme_3 = Filme('O Poderoso Chefão', 'Francis Ford Coppola')
    
    filmes = [filme_1, filme_2, filme_3]
    
    return filmes

def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    return filme_procurado in meus_filmes


meus_filmes = pega_todos_os_filmes()
for filme in meus_filmes:
    print(filme)

filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')

if tenho_o_filme(filme_procurado):
    print('Tenho o filme!')
else:
    print('Não tenho :(')