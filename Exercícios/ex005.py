# Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
# sucessor.
# Ex:
# Digite um número: 9
# O antecessor de 9 é 8
# O sucessor de 9 é 10

n = int(input('Digite um número: '))
print('O antecessor de {} é'.format(n), n - 1)
print('O sucessor de {} é'.format(n), n + 1)

