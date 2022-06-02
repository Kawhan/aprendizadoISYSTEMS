import os
print(os.getcwd())
print()
livros = []

with open('os.path.join(livros.txt)', "r") as arquivo:
    for linha in arquivo:
        print(linha)
        linha  = linha.strip()
        livros.append(linha)
        
    print(livros)    