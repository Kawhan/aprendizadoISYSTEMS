class Conta:
    # Construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o o objeto {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    # Metodos
    def extrato(self):
        print(f"\nO saldo de {self.__saldo} do títular {self.__titular}.\n")
    
    def deposito(self, valor):
        self.__saldo += valor
        
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_saque
        
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor passou o limite")
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposito(valor)
        
    # Gets
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular        
    
    @property
    def limite(self):
        return self.__limite

    # static methods
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
    
    # Sets
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        


print(Conta.codigo_banco())
print(Conta.codigos_bancos())

# conta.saca(100.0)
# print(conta.saldo)

# print(conta.limite)
# conta.limite = 10000.0
# print(conta.limite)



# conta.extrato()
# conta2.extrato()

# conta.transfere(30, conta2)


# conta.extrato()
# conta2.extrato()

# conta.deposito(20)
# conta.extrato()
# conta.saca(20)
# conta.extrato()

# conta2.deposito(20)
# conta2.extrato()
# conta2.saca(20)
# conta2.extrato()