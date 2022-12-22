# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Minha resolução do exercício.
from math import factorial
num = int(input('''
Digite um número para
calcular seu Fatorial:
>>> '''))
f = factorial(num)
print('Calculando {}! ='.format(num), end='')
while num != 0:
    if num > 1:
        print(' {} x'.format(num), end='')
    elif num == 1:
        print(' {} = '.format(num), end='')
    num -= 1
print(f)

'''
# Resolução do exercício pelo professor.
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''