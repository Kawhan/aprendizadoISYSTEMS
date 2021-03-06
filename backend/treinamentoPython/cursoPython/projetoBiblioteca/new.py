#!/bin/python3
# -*- coding: utf-8 -*-
# Problema 1
#
# Complete a função 'sort_string_as_number' abaixo.
#
# A função aceita um array de string como parametro.
# Os elementos sempre começam com 'person_' seguido por um numero. Ex. 'person_8', 'person_1234'.
#
# A função deve retornar o array de entrada ordenado pelos numeros no final de cada elemento.
# Exemplo: O retorno para a entrada ['person_8', 'person_80', 'person_9'] deve ser ['person_8', 'person_9', 'person_80'].
#
# Exemplo de saida: ['person_8', 'person_9', 'person_80']
#



def sort_string_as_number(arr):
    escolhida = '' 
    maior = ''
    menor = None
    list = []
    
    # Escreve seu código abaixo
    for i in range(len(arr)):
        for palavra in arr:  
            number = int(palavra[7:])  
            if  menor == None:
                menor = number
                escolhida = palavra
            elif number <= menor:
                menor = number
                escolhida = palavra
            else:
                maior = number

        list.append(f"person_{menor}")
        arr.remove(escolhida)
        menor = maior
    
    return list
# Problema 2
#
# Complete a função 'stair_draw' abaixo.
# 
# A função aceita um inteiro como parametro que define o tamanho da base da escada.
# A função vai usar o simbolo # para desenhar uma escada.
# Exemplo de saida para base igual 3.
'''
  #
 ##
###
'''

'''
Com as mudanças para aparecer a escada do mario


     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######
'''
def stair_draw(n):
    
    string = ""
    
    # Escreve seu código abaixo
    cont = 0
    while (n >= 0):
        if cont ==0:
            pass
        else:
            if cont != 6:
                string += f"""{" "*(n)}{"#"*cont}"""
                string += f""" {"#"*cont}"""
                string += "\n"
            else:
                string += f"""{" "*(n)}{"#"*cont}"""
                string += f""" {"#"*cont}"""
        n -= 1
        cont += 1

    
    return string
# Problema 3
#
# Complete a função 'compare_skills' abaixo.
# 
# A função recebe dois arrays de inteiros como parametro, cada um contendo 3 posições. Ex. [3, 4, 18] e [14, 4, 1]
# Cada posição representa os pontos de habilidade de uma pessoa em linguagens de programação como: [python, php, javascript].
#
# O parametro 'a' representa a pontuação de João, e o parametro 'b' representa a pontuação da Maria.
# A tarefa é comparar as pontuações de cada habilidade de João e Maria: a[0] com b[0], a[1] com b[1], a[2] com b[2].
# Se a[i] > b[i], então João ganha 1 ponto. 
# Se a[i] < b[i], então Maria ganha 1 ponto. 
# Se a[i] = b[i], então ninguém ganha ponto. 
#
# Veja o exemplo abaixo:
#
# a = [3, 4, 8] 
# b = [1, 5, 9]
# 
# Na posição 0 João ganha 1 ponto. Na posição 1 Maria ganha 1 ponto. Na posição 2 Maria ganha 1 ponto.
# O resultado da função é um array com valores [1, 2], onde 1 é a soma dos pontos de João e 2 é a soma dos pontos de Maria.
# Maria ficou em primeiro e João em segundo. 
#
# Exemplo de saida: [1, 2]
#
def compare_skills(a, b):
    
    list_pontos = [0,0]
    
    # Escreve seu código abaixo
    for numero in a:
        for numero2 in b:
            if numero > numero2:
                list_pontos[0] += 1
            if numero < numero2:
                list_pontos[1] += 1
            b.remove(numero2)
            break
            
    return list_pontos
# Problema 4
#
# Complete a função 'diagonal_diff' abaixo.
#
# Calcule a diferença absoluta entre as somas das diagonais de uma matriz quadrada.
# Exemplo de matriz quadrada de ordem 4:
#
# 1 2 3 1
# 4 5 6 2
# 9 8 9 2
# 2 4 1 3
#
# Diagonal da esquerda para a direita = 1 + 5 + 9 + 3 = 18
# Diagonal da direira para a esquerda = 1 + 6 + 8 + 2 = 17
#
# O retorno da função é a diferença absoluta: 18 - 17 = 1.
# Exemplo de saida: 1
#
def diagonal_diff(arr):
    
    escolha = 0
    escolha2 = -1
    listarr = []
    listarr2 = []
    # Escreve seu código abaixo
    for espacos in arr:
        listarr.append(espacos[escolha])
        escolha += 1
    
    for espacos in arr:
        listarr2.append(espacos[escolha2])
        escolha2 -= 1
    
    
    
    return abs(sum(listarr) - sum(listarr2))
# Problema 5
#
# Complete a função 'perc_elements' abaixo.
#
# Dado um array de inteiros, calcule a proporção de elementos positivos, negativos e zeros.
# Exemplo de array de entrada: [1, 1, 0, -1, -1]
#
# Dos 5 elementos do array, temos 2 inteiro, 2 negativos e 1 zero.
# Nesse exemplo a função deve retornar um array com a proporção de cada tipo, com uma precisão de 6 casas decimais.
# 
# O retorno deve ser um array com 3 posições um para cada tipo: [positivo, negativo, zero]
# Exemplo de saida: [0.400000, 0.400000, 0.200000]
#
def perc_elements(arr):
    
    # Escreve seu código abaixo
    possitivos = 0
    negativos = 0
    zeros = 0
    
    tamanho = len(arr)
    
    for elemento in arr:
        if (elemento > 0):
            possitivos += 1
        elif (elemento < 0):
            negativos += 1
        elif (elemento == 0):
            zeros += 1
    
    
    return [round(possitivos/tamanho, 6), round(negativos/tamanho,6), round(zeros/tamanho, 6)]

if __name__ == '__main__':
    # sort_string_as_number()
    arr = ['person_1', 'person_2', 'person_3', 'person_10', 'person_100', 'person_31', 'person_22']
    res = sort_string_as_number(arr)
    print(res)
    # stair_draw()
    n = 6
    res = stair_draw(n)
    print(res)
    # compare_skills()
    joao = [17, 28, 30]
    maria = [99, 16, 8]
    res = compare_skills(joao, maria)
    print(res)
    
    # diagonal_diff()
    arr = [[1, 2, 3, 1], [4, 5, 6, 2], [9, 8, 9, 2], [2, 4, 1, 3]]
    res = diagonal_diff(arr)
    print(res)
    
    # perc_elements
    arr = [1, 1, 0, -1, -1]
    res = perc_elements(arr)
    print(res)