#Módulos
import sys
import pygame
import random

#Número de Jogadores
while(True):
    try:
        numeroJogadores = int(input("Número de Jogadores: "))
        if numeroJogadores >= 2 and numeroJogadores <= 4:
            break
        else:
            print("Número de Jogadores tem de estar compreendido entre 2 e 4")
    except:
        print("Insere apenas números inteiros.")

#Nomes dos Jogadores 
nomesJogadores = []
for i in range(numeroJogadores):
    nome = input("Nome do Jogador {0}: ".format(i + 1))
    nomesJogadores.append(nome)

#Jogador da Palavra
randomizador = random.randint(1, numeroJogadores)

if randomizador == 1:
    print("O jogador {0} escolhe a palavra".format(randomizador))

if randomizador == 2:
    print("O jogador {0} escolhe a palavra".format(randomizador))

if randomizador == 3:
    print("O jogador {0} escolhe a palavra".format(randomizador))

if randomizador == 4:
    print("O jogador {0} escolhe a palavra".format(randomizador))
