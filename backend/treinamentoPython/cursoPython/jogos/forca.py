import random

def jogar_forca():
    print_msg_start()
    
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = iniciar_letras_acertadas(palavra_secreta)
    
    enforocou = False
    acertou = False
    tentativas = 0
    
    print(letras_acertadas)
    
    # enquanto não enforocou e não acertou
    while(not enforocou and not acertou):
        
        chute = input("\nQual letra? ")
        chute = chute.strip().upper()
        
        index = 0
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                # Retirando os espaços
                letra = letra.strip()
                
                
                if (letra == chute):
                    letras_acertadas[index] = chute
                    
                index += 1
        else:
            print(f"\nQue pena, você errou! Faltam {6 - tentativas}")
            tentativas += 1
        
        enforocou = tentativas == 6
        acertou  = "_" not in letras_acertadas
        print("\n", letras_acertadas)

    if(acertou):
        print("\nVocê ganhou!")
    else:
        print("\nVocê perdeu!")
    print("\nFim do jogo!")


def iniciar_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def print_msg_start():
    print("################################")
    print("***Bem vindo no jogo da forca***")
    print("################################\n")


def carrega_palavra_secreta():
    palavras = []
    
    with open("./palavras/palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha  = linha.strip()
            palavras.append(linha)
            
    numero_aleatorio = random.randrange(0, len(palavras))
    
    palavra_secreta = palavras[numero_aleatorio].upper()
    
    return palavra_secreta


if (__name__ == "__main__"):
    jogar_forca()