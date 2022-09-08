# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex:
# Digite um número real: 5.25
# O número interio de 5.25 é 5.

# import math
# num = float(input('Digite um número real: '))
# print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))
# Funciona também com a função "floor(num)".

num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}'.format(num, int(num)))
