# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()
lista = cidade.split()
print(lista)
print('SANTO' in lista[0])