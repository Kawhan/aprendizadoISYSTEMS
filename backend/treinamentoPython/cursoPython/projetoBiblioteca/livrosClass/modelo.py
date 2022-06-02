class Livros:
    def __init__(self, nome, autor, data_publicacao):
        self._nome = nome
        self._autor = autor
        self._data_publicacao = data_publicacao
    
    def __str__(self):
        return f'Nome do livro: {self._nome} - Autor: {self._autor} - Data publicação: {self._data_publicacao}'
    
#
    
    
class Biblioteca():
    def pegarLivros(self):
        livros = []
                    
        with open('livros.txt', "r") as arquivo:
            for linha in arquivo:
                linha  = linha.strip()
                livros_montagem = linha.split(' - ')
                book = Livros(livros_montagem[0], livros_montagem[1], livros_montagem[2])
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
        
        with open('livros.txt', "a") as arquivo:
            arquivo.write(f"\n{nome} - {autor} - {data_de_publicacao}")
            


livros = Biblioteca()


livros.adicionarLivros()


   
