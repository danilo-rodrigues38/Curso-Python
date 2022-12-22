# Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e sorteando o nome do escolhido.
import random

print('SORTEIO'.center(20))
print('-' * 20)
al1 = input('Nome do 1º aluno: ')
al2 = input('Nome do 2º aluno: ')
al3 = input('Nome do 3º aluno: ')
al4 = input('Nome do 4º aluno: ')
esc = random.choice([al1, al2, al3, al4])
print('-' * 20)
print('O aluno escolhido foi {}'.format(esc))
