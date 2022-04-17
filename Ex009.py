# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua taboada.

i = 1
print('Vamos fazer uma taboada')
n = int(input('Digite um valor: '))
print('-' * 11)
while (i <= 10):
    t = n * i
    print('{} * {:2} = {:2}'.format(n, i, t))
    i = i + 1

print('-' * 11)

