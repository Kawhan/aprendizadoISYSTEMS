import json
from time import process_time_ns

class Livros:
    def __init__(self, nome, autor, data_publicacao):
        self._nome = nome
        self._autor = autor
        self._data_publicacao = data_publicacao
    
    def __str__(self):
        return f'Nome do livro: {self._nome} - Autor: {self._autor} - Data publicação: {self._data_publicacao}'
    
    # 
    def __eq__(self, outro_filme_nome):
        return self._nome == outro_filme_nome
    
    def __ne__(self, outro_filme_nome):
        return self._nome != outro_filme_nome
    
    @property
    def nome(self):
        return self._nome
    
    
class Biblioteca():
    def pegarLivros(self):
        livros = []
                    
        with open('livros.txt', "r") as arquivo:
            for linha in arquivo:
                linha  = linha.strip()
                livros_montagem = linha.split(' - ')
                if [0, 1, 2] in livros_montagem:    
                    book = Livros(livros_montagem[0], livros_montagem[1], livros_montagem[2])
                    livros.append(book)
                else:
                    print("erro")
        
        return livros
        
    def listarLivros(self):
        lista_livros = self.pegarLivros()
        print("\nListando os Livros\n")
        for livro in lista_livros:
            print(livro)
    
    def adicionarLivros(self):
        print("Bem vindo a Biblioteca pessoal, digite o livro que você quer cadastrar: ")
        nome = ""
        autor = ""
        data_de_publicacao = ""
        while(nome == "" or autor == "" or data_de_publicacao == ""):
            nome = input("Digite o nome do seu livro: ")
            autor = input("Digite o autor do seu livro: ")
            data_de_publicacao = input("Digite a data de publicação do seu livro: ")
            
            nome = nome.title().strip()
            autor = autor.title().strip()
            data_de_publicacao = data_de_publicacao.strip()
        
        list = []
        
         
        with open('livros.json') as arquivo_json:
            if arquivo_json:
                arquivo_json_text = json.load(arquivo_json)
            
                
        
        for line in arquivo_json_text:
            list.append(line)
        
        with open('livros.json', "w") as arquivo:
            livro_dict = {"Nome": nome, "Autor": autor, "Data de publicação": data_de_publicacao}
            list.append(livro_dict)
            text_json = json.dumps(list)
            print(text_json)
            arquivo.write(text_json)
            
    def removerLivros(self):
        livro_remove = input("Bem vindo a Biblioteca pessoal, digite o nome do livro que você quer remover: ")
        livro_remove = livro_remove.title().strip()
        
        lista_livros = self.pegarLivros()
        cont = 0
        for livro in lista_livros:
            if (livro_remove == livro.nome):
                lista_livros.pop(cont)
                self.removeLinha(cont)
                
                    
            cont += 1
        
    def removeLinha(self, indice):
        with open('livros.txt', "r") as arquivo:
            livroLinhas = arquivo.readlines()
        
        livroLinhas.pop(indice)
        
        with open("livros.txt", "w") as f:
            for line in livroLinhas:
                f.write(line)
            
        

livros = Biblioteca()

livross = livros.adicionarLivros()
