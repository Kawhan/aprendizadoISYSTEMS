import jsonlibrary

def interfaceLibrary():
    print("################################")
    print("*******Bem vindo a livraria*******")
    print("################################\n")
    
    print("Digite o número correspondente a sua operação")
    print("(1) Listar Livros | (2) Adicionar Livro | (3) Remover Livro")
    
    operacao = int(input(""))
    continuar = True
    livros = jsonlibrary.Biblioteca()
    
    while continuar:
        if (operacao == 1):
            livros.listarLivros()
        elif (operacao == 2):
            livros.adicionarLivros()
        elif (operacao == 3):
            livros.removerLivros()
        else:
            print("\nNúmero invalido para operação configura novamente as opções")
        
        confirma = input("\nDeseja fazer outra operação? ('SIM') ou ('Não')")
        if (confirma != "Não" and confirma != "Nao"):
            print("\n(1) Listar Livros | (2) Adicionar Livro | (3) Remover Livro")
            operacao = int(input(""))
        else:
            continuar = False

if(__name__ == "__main__"):
    interfaceLibrary()