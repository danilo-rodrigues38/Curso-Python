#  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for index in range(1, 7):
    n = int(input('Digite o {}º número: '.format(index)))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares digitados é {}.'.format(soma))
