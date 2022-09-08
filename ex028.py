# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# import random   # Carrega toda a biblioteca 'RANDOM'
# import time     # Carraga toda a biblioteca 'TIME'
# PARA NÃO PRECISAR IMPORTAR TODA A BIBLIOTECA, POIS SOMENTE USAREMOS DUAS FUNÇÕES,
# UTILIZAREMOS OS COMANDOS ABAIXO:

from random import randint
from time import sleep

print('Vamos jogar!!!')
print('-' * 14)
print()
print('O computador vai escolher um número aleatório \nentre 0 e 5 e você deverá acertar qual é o número.\nVamos lá!!!')
print()
n1 = int(input('Digite um número? '))
n2 = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
print()
print('O número sorteado pelo computador foi {}.'.format(n2))
if n1 == n2:
    print('Parabéns!!! você adivinhou o número!')
else:
    print('Não foi desta vez.\nTente novamente!!!')

