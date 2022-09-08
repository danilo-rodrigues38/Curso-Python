# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('\nFormará um triângulo do tipo:')
    if r1 == r2 == r3:
        print('EQUILÁTERO: todos os lados iguais.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES: dois lados iguais, um diferente.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO: todos os lados diferentes.')
else:
    print('\nElas não podem formar um triângulo.')
