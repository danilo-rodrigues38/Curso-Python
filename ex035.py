# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Elas podem formar um triângulo.')
else:
    print('Elas não podem formar um triângulo.')
