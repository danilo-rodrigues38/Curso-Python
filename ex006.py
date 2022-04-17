# Crie um algoritmo que leia um número real e mostre na tela o seu dobro, o seu triplo e
# sua raiz quadrada.
# Ex:
# Digite um número: 9
# O dobro de 9 é 18
# O triplo de 9 é 27
# A raiz quadrada de 9 é 3

n = int(input('Digite um número: '))
print('O dobro de {} é {}.'.format(n, (n*2)))
print('O triplo de {} é {}.'.format(n, (n*3)))
print('A raiz quadrada de {} é {:.2f}.'.format(n, n**(1/2)))
print('A raiz quadrada de {} é {:.2f}.'.format(n, pow(n, (1/2)))) # Função de power "pow(n, (1/2)" para raiz quadrada.

