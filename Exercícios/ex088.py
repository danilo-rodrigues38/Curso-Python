# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
listamega = list()
numeros = list()
print('-' * 40)
print('JOGA NA MEGA SENNA'.center(40))
print('-' * 40)
num = int(input('Quantos jogos você que que eu sorteie? '))
for cont in range(0, num):
    while True:
        n = randint(1, 60)
        if n not in numeros:
            numeros.append(n)
        if len(numeros) == 6:
            break
    numeros.sort()
    listamega.append(numeros[:])
    numeros.clear()
print(f' SORTEANDO {num} JOGOS '.center(40, '-'))
for cont in range(0, num):
    print(f'Jogo {cont + 1}:', end='')
    print(listamega[cont])
    sleep(1)
print('< BOA SORTE >'.center(40, '-'))
