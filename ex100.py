# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somapar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}, ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores de {lista}, temos {soma}.')


#Programa principal
numeros = list()
sorteio(numeros)
somapar(numeros)
