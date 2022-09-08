# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for cont in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        else:
            maior = peso
print('O maior peso digitado foi {} kilos.'.format(maior))
print('O menor peso digirado foi {} kilos.'.format(menor))
