# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

# Primeiro analisar o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Segundo analisar o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Agora mostramos o resultado
print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))
