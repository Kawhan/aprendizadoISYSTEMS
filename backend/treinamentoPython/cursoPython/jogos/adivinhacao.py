def jogar_adivinhacao():
    import random

    print("################################")
    print("Bem vindo no jogo de adivinhacao")
    print("################################\n")

    numero_secreto = random.randrange(1, 101)
    numero_maior = 100
    numero_menor = 1
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícl")

    nivel = int(input("Digite o nível: "))

    while (nivel <= 0 or nivel >= 3):
        print("\nNível invalido!")
        print("(1) Fácil (2) Médio (3) Difícl")
        nivel = int(input("\nDigite o nível: "))
        
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    elif (nivel == 3):
        total_tentativas = 5
        

    for rodada in range(1,total_tentativas + 1):
        print(f"\nTentativa: {rodada} de {total_tentativas}" )
        chute_str  = input("Digite seu número entre 1 e 100: ")

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue
            
        acertou  = chute ==  numero_secreto
        maior = chute > numero_secreto
        menor  = chute < numero_secreto
        
        if (acertou):
            print(f"\nVocê acertou! E seu score foi {pontos}")
            break
        else:
            if (maior):
                numero_maior = chute
                print("\nVocê errou! Seu chute foi maior que o do número secreto!")
                print(f"Seu número está entre {numero_menor} e {numero_maior}")
            elif (menor):
                numero_menor = chute
                print("\nVocê errou! Seu chute foi menor que o do número secreto!")
                print(f"Seu número está entre {numero_menor} e {numero_maior}")
            pontos_perdidos = abs(numero_menor - chute)
            pontos -= pontos_perdidos
        

    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar_adivinhacao()