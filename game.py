#Módulos
import sys
import pygame
import random

numeroJogadoresCheck = True

#Verificação de Inserção de Número de Jogadores (2-4)
while(numeroJogadoresCheck):

    numeroJogadores = input("Número de Jogadores: ")
    numeroJogadores = int(numeroJogadores)

    if (numeroJogadores == 1):
        print("Este jogo não se pode jogar sozinho :c")
    else:
        if (numeroJogadores == 2):
            numeroJogadoresCheck = False
        else:
            if (numeroJogadores == 3):
                numeroJogadoresCheck = False
            else:
                if (numeroJogadores == 4):
                    numeroJogadoresCheck = False
                else:
                    print("O número de jogadores tem que estar compreendido entre 2 e 4")

#Nomes dos Jogadores
nomeJogador1 = "Por Definir"
nomeJogador2 = "Por Definir"
nomeJogador3 = "Por Definir"
nomeJogador4 = "Por Definir"

if numeroJogadores == 2:
    nomeJogador1 = input("Nome do jogador 1: ")
    nomeJogador2 = input("Nome do jogador 2: ")

if numeroJogadores == 3:
    nomeJogador1 = input("Nome do jogador 1: ")
    nomeJogador2 = input("Nome do jogador 2: ")
    nomeJogador3 = input("Nome do jogador 3: ")

if numeroJogadores == 4:
    nomeJogador1 = input("Nome do jogador 1: ")
    nomeJogador2 = input("Nome do jogador 2: ")
    nomeJogador3 = input("Nome do jogador 3: ")
    nomeJogador4 = input("Nome do jogador 4: ")

#Escolha do Jogador que escolhe a palavra
randomizador = random.randint(1, numeroJogadores)

if randomizador == 1:
    print("O jogador {0} escolhe a palavra".format(randomizador))

if randomizador == 2:
    print("O jogador {0} escolhe a palavra".format(randomizador))

if randomizador == 3:
    print("O jogador {0} escolhe a palavra".format(randomizador))

if randomizador == 4:
    print("O jogador {0} escolhe a palavra".format(randomizador))
