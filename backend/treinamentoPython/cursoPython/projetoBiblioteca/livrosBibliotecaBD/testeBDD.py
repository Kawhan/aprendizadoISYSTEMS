import mysql.connector
from functools import total_ordering

cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='BIBLIOTECA', port=3305)

@total_ordering
class Livros:
    def __init__(self, nome, autor, data_publicacao):
        self._nome = nome
        self._autor = autor
        self._data_publicacao = data_publicacao
    
    def __str__(self):
        return f'Nome do livro: {self._nome} - Autor: {self._autor} - Data publicação: {self._data_publicacao}'
    
    # 
    def __eq__(self, outro_livro):
        if isinstance(outro_livro, Livros):
            return ((self._nome == outro_livro._nome) and 
                    (self._autor == outro_livro._autor) and 
                    (self._data_publicacao == outro_livro._data_publicacao))
        
        return False
    
    def __lt__(self, outro_livro):
        return self._data_publicacao > outro_livro._data_publicacao
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def data_publicacao(self):
        return self._data_publicacao
    
    
class Biblioteca():
    def pegarLivros(self):
        livros = []
        
        mycursor = cnx.cursor()
                    
        # with open('livros.json', "r") as arquivo:
        #     for linha in arquivo:
        #         linha  = linha.strip()
        #         livros_montagem = linha.split(' - ')
        #         if [0, 1, 2] in livros_montagem:    
        #             book = Livros(livros_montagem[0], livros_montagem[1], livros_montagem[2])
        #             livros.append(book)
        #         else:
        #             print("erro")
        
        mycursor.execute("SELECT * FROM livros")

        myresult = mycursor.fetchall()
       

        for x in myresult:
            book = Livros(x[0], x[1], x[2])
            livros.append(book)
        
        mycursor.close()
        return livros
        
    def listarLivros(self):
        lista_livros = self.pegarLivros()
        print("\nListando os Livros\n")
        for livro in sorted(lista_livros):
            print(livro)
    
    def adicionarLivros(self):
        print("\nBem vindo a Biblioteca pessoal, digite o livro que você quer cadastrar: \n")
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
        
        
        
        self.adicionarLinha(nome, autor, data_de_publicacao)
        
        print("\nLivro adicionado com sucesso :)")
        
    def CriarLivro(self, nome, autor, data_de_publicacao):
        nome = nome.title().strip()
        autor = autor.title().strip()
        data_de_publicacao = data_de_publicacao.title().strip()
        
        book = Livros(nome, autor, data_de_publicacao)
        
        return book
    
    
    def removerLivros(self):
        print("\nBem vindo a Biblioteca pessoal, digite o livro que você quer remover: \n")
        livro_remove_nome = input("Digite o nome do livro que você quer remover: ")
        livro_remove_autor = input("Digite o autor do livro que você quer remover: ")
        livro_remove_data = input("Digite a data de publicação do livro que você quer remover: ")
        
        book = self.CriarLivro(livro_remove_nome, livro_remove_autor, livro_remove_data)
        
        lista_livros = self.pegarLivros()
        cont = 0
        autorizado = False
        for livro in lista_livros:
            if (book == livro):
                self.removeLinha(livro)
                autorizado = True
                
          
            cont += 1

        if (not autorizado):
            pergunta = input("Livro não encontrado, deseja fazer a operação de novo? ('SIM') ou ('Não')")
            pergunta = pergunta.strip().title()
            if (pergunta != "Não" and pergunta != "Nao"):
                self.removerLivros()

        print("\nOperação de remoção completa :)")
        
    def removeLinha(self, book):
        # with open('livros.txt', "r") as arquivo:
        #     livroLinhas = arquivo.readlines()
        
        # livroLinhas.pop(indice)
        
        # with open("livros.txt", "w") as f:
        #     for line in livroLinhas:
        #         f.write(line)
        
        mycursor = cnx.cursor()

        sql = f"DELETE FROM livros WHERE NOME = '{book.nome}' and AUTOR = '{book.autor}' and DATA_DE_PUBLICACAO = '{book.data_publicacao}'"

        mycursor.execute(sql)

        cnx.commit()
    
    def adicionarLinha(self,nome, autor, data_de_publicacao):
        mycursor = cnx.cursor()
        
        sql = "INSERT INTO livros (NOME, AUTOR, DATA_DE_PUBLICACAO) VALUES (%s, %s, %s)"
        val = (nome, autor, data_de_publicacao)

        mycursor.execute(sql, val)
        
        cnx.commit()
        mycursor.close()
    
    def update_book(self):
        print("\nBem vindo a Biblioteca pessoal, digite o livro que você quer mudar: \n")
        livro_update_nome = input("Digite o nome do livro que você quer mudar: ")
        livro_updade_autor = input("Digite o autor do livro que você quer mudar: ")
        livro_update_data = input("Digite a data de publicação do livro que você quer mudar: ")
        
        book = self.CriarLivro(livro_update_nome, livro_updade_autor, livro_update_data)
        
        livro_update_nome2 = input("\nDigite o nome do livro que você quer atribuir: ")
        livro_updade_autor2 = input("Digite o autor do livro que você quer atribuir: ")
        livro_update_data2 = input("Digite a data de publicação do livro que você quer atribuir: ")
        
        book2 = self.CriarLivro(livro_update_nome2, livro_updade_autor2, livro_update_data2)
        
        lista_livros = self.pegarLivros()
        cont = 0
        autorizado2 = False
        for livro in lista_livros:
            if (book == livro):
                self.atualizaLinha(livro, book2)
                autorizado2 = True
        
            cont += 1    
        
        if (not autorizado2):
            pergunta = input("Livro para mudança não encontrado, deseja fazer a operação de novo? ('SIM') ou ('Não')")
            pergunta = pergunta.strip().title()
            if (pergunta != "Não" and pergunta != "Nao"):
                self.update_book()

        print("\nOperação de update completa :)")
          
    def atualizaLinha(self, book, book2):
        # with open('livros.txt', "r") as arquivo:
        #     livroLinhas = arquivo.readlines()
        
        # livroLinhas.pop(indice)
        
        # with open("livros.txt", "w") as f:
        #     for line in livroLinhas:
        #         f.write(line)
        
        mycursor = cnx.cursor()

        # sql = f"UPDATE FROM livros WHERE NOME = '{book.nome}' and AUTOR = '{book.autor}' and DATA_DE_PUBLICACAO = '{book.data_publicacao}'"
        sql = f"UPDATE livros SET NOME = '{book2.nome}', AUTOR = '{book2.autor}', DATA_DE_PUBLICACAO = '{book2.data_publicacao}' WHERE NOME = '{book.nome}' and AUTOR = '{book.autor}' and DATA_DE_PUBLICACAO = '{book.data_publicacao}'"

        mycursor.execute(sql)

        cnx.commit()
            