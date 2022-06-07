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
                    
        # with open('livros.json', "r") as arquivo:
        #     for linha in arquivo:
        #         linha  = linha.strip()
        #         livros_montagem = linha.split(' - ')
        #         if [0, 1, 2] in livros_montagem:    
        #             book = Livros(livros_montagem[0], livros_montagem[1], livros_montagem[2])
        #             livros.append(book)
        #         else:
        #             print("erro")
        
        with open("livros.json", "r+", encoding="utf-8") as dados:
            texto_json = json.load(dados)
        
        for data in texto_json:
            book = Livros(data['Nome'], data['Autor'], data['Data de publicação'])
            livros.append(book)
        
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
        with open("livros.json", "r+", encoding="utf-8") as dados:
            texto_json = json.load(dados)
        
        for line in texto_json:
            list.append(line)
        
                
        with open('livros.json', "w", encoding="utf-8") as arquivo:
            livro_dict = {"Nome": nome, "Autor": autor, "Data de publicação": data_de_publicacao}
            list.append(livro_dict)
            text_json = json.dumps(list)
            arquivo.write(text_json)
            
    def removerLivros(self):
        livro_remove = input("Bem vindo a Biblioteca pessoal, digite o nome do livro que você quer remover: ")
        livro_remove = livro_remove.title().strip()
        
        lista_livros = self.pegarLivros()
        cont = 0
        autorizado = False
        for livro in lista_livros:
            if (livro_remove == livro.nome):
                lista_livros.pop(cont)
                self.removeLinha(cont)
                autorizado = True
                
          
            cont += 1

        if (not autorizado):
            pergunta = input("Livro não encontrado, deseja fazer a operação de novo? ('SIM') ou ('Não')")
            pergunta = pergunta.strip().title()
            if (pergunta != "Não" and pergunta != "Nao"):
                self.removerLivros()

        
    def removeLinha(self, indice):
        # with open('livros.txt', "r") as arquivo:
        #     livroLinhas = arquivo.readlines()
        
        # livroLinhas.pop(indice)
        
        # with open("livros.txt", "w") as f:
        #     for line in livroLinhas:
        #         f.write(line)
        
        list = []
        with open("livros.json", "r+", encoding="utf-8") as dados:
            texto_json = json.load(dados)
        
        for line in texto_json:
            if line != texto_json[indice]:
                list.append(line)
        
        with open('livros.json', "w", encoding="utf-8") as arquivo:
            text_json = json.dumps(list)
            arquivo.write(text_json)
            
        

livros = Biblioteca()

# livross = livros.listarLivros()
livros.adicionarLivros()
