# Escreva um programa que leia um número N inteiro qualquer e mostre na
# tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('\033[32m')
print('*' * 30)
print('Sequencia de Fibonacci'.center(30))
print('*' * 30)
print('\033[m')

se = int(input('Digite quantos elementos quer ver: '))
t1 = 0
t2 = 1
t3 = 0
cont = 3
print('{} - {}'.format(t1, t2), end=' - ')
while cont <= se:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{}'.format(t3), end=' - ')
    cont += 1
print('Fim da sequencia.')
