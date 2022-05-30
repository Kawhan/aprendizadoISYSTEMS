from http import client


class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        print("\nChamando metodo get ou @property nome()")
        # title garante que a primeira letra é sempre maiúscula
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        print("\nChamando o setter nome()")
        self.__nome = nome
        

cliente = Cliente("kawhan")

print(cliente.nome)        
cliente.nome = "Laurindo"
print(cliente.nome)