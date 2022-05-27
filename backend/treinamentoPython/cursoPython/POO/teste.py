

def criar_conta(numero, titular, saldo, limite):
    conta  = {"numero": numero, "titular": titular, "Saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["Saldo"] +=  valor
    
def saque(conta, valor):
    conta["Saldo"] -=  valor

def extrato(conta):
    saldo = conta["Saldo"]
    print(f"Saldo da sua conta é { saldo }")