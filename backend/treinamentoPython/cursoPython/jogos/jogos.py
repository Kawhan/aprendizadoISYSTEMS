import adivinhacao
import forca

def escolhe_jogo():
    print("################################")
    print("*******Escolha o seu jogo*******")
    print("################################\n")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar_forca()
    else:
        print("Jogando adivinhação\n")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()