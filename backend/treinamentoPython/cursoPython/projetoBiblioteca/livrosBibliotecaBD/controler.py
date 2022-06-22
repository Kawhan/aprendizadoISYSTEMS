from ast import Raise
from multiprocessing.sharedctypes import Value
import testeBDD

def interfaceLibrary():
    print("################################")
    print("*******Bem vindo a livraria*******")
    print("################################\n")
    
    print("Digite o número correspondente a sua operação")
    print("(1) Listar Livros | (2) Adicionar Livro | (3) Remover Livro | (4) Atualizar(UPDATE) Livro | (5) Sair")
    
    while True:
        try:
            operacao = int(input(""))
            continuar = True
            livros = testeBDD.Biblioteca()
            break
        except:
            print("Valor invalido: Digite novamente outro valor")
            print("Digite o número correspondente a sua operação")
            print("(1) Listar Livros | (2) Adicionar Livro | (3) Remover Livro | (4) Atualizar(UPDATE) Livro | (5) Sair")
    
    while continuar:
        if (operacao == 1):
            livros.listarLivros()
        elif (operacao == 2):
            livros.adicionarLivros()
        elif (operacao == 3):
            livros.removerLivros()
        elif (operacao == 4):
            livros.update_book()
        elif (operacao == 5):
            print("Saindo do sistema! Obrigado")
            break
        else:
            print("\nNúmero invalido para operação configura novamente as opções")
        
        
        confirma = input("\nDeseja fazer outra operação? ('SIM') ou ('Não') ").strip()
        if (confirma.lower() == 's' or confirma.lower() == 'sim'):
            print("\n(1) Listar Livros | (2) Adicionar Livro | (3) Remover Livro | (4) Atualizar(UPDATE) Livro | (5) Sair")
            operacao = int(input(""))
        else:
            continuar = False

if(__name__ == "__main__"):
    interfaceLibrary()