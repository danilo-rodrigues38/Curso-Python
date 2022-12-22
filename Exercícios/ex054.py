# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
maior = 0
menor = 0
ano = datetime.today().year

for cont in range(1, 8):
  # nome = str(input('\nDigite o nome da {}ª pessoa: '.format(cont)))
    nasc = int(input('Digite o ano de nascimento: '))
    if (ano - nasc) >= 21:
        maior += 1
    else:
        menor += 1
print('A total de maiores é {} e o total de menores é {}.'.format(maior, menor))