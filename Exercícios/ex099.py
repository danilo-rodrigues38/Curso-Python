# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    cont = mai = 0
    print('-=' * 30)
    print("Analizando os valores passados... ", end='')
    for valor in num:
        print(f'\033[33m{valor}\033[m', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'\nForam informados \033[31m{len(num)}\033[m valores ao todo.')
    print(f'O maio valor informado foi \033[32m{mai}\033[m.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
