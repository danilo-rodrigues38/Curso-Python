# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
cont = 0
while True:
    num = int(input('Digite um valor (999 para sair): '))
    if num == 999:
        break
    lista.append(num)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'A lista ordenada de forma decrescente é {lista}.')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
