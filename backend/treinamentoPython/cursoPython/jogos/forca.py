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
        
        chute = carrega_chute()
        
        
        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas += 1
            desenha_forca(tentativas)
        
        enforocou = tentativas == 7
        acertou  = "_" not in letras_acertadas
        print("\n", letras_acertadas)

    imprime_mensagem(acertou, palavra_secreta)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem(acertou, palavra_secreta):
    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
                # Retirando os espaços
                letra = letra.strip()
                
                
                if (letra == chute):
                    letras_acertadas[index] = chute
                    
                index += 1

def carrega_chute():
    chute = input("\nQual letra? ")
    chute = chute.strip().upper()
    return chute

def iniciar_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def print_msg_start():
    print("################################")
    print("***Bem vindo no jogo da forca***")
    print("################################\n")


def carrega_palavra_secreta():
    palavras = []
    
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha  = linha.strip()
            palavras.append(linha)
            
    numero_aleatorio = random.randrange(0, len(palavras))
    
    palavra_secreta = palavras[numero_aleatorio].upper()
    
    return palavra_secreta

if (__name__ == "__main__"):
    jogar_forca()