# O memso professor anterior que sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('ORDENAÇÃO'.center(20))
print('-' * 20)
al1 = input('Nome do 1º aluno: ')
al2 = input('Nome do 2º aluno: ')
al3 = input('Nome do 3º aluno: ')
al4 = input('Nome do 4º aluno: ')
print('-' * 20)
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
