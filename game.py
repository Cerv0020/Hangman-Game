#Módulos
import sys
import pygame
import getpass
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
print("Nome do jogador que irá escolher a palavra :" + nomesJogadores[randomizador - 1])
palavra = getpass.getpass('Palavra: ')

#Adivinha a palavra
while(True):
    try:
        letra = input("Letra: ")
        if letra.isalpha():
            print("É letra")
            break   
        else:
            print("Só letras podem ser introduzidas")
    except:
        print()
