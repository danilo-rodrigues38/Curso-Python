# Faça um programa que leia cinco valores núméricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = []
for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 30)
maior = menor = 0
print(f'Você digitou os valores {num}')
for n in range(0, len(num)):
    if n == 0:
        maior = menor = num[n]
    if num[n] > maior:
        maior = num[n]
    if num[n] < menor:
        menor = num[n]
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, n in enumerate(num):
    if n == maior:
        print(f'{p}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p, n in enumerate(num):
    if n == menor:
        print(f'{p}...', end=' ')
print()
