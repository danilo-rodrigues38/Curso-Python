# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).strip().lower()
print(nome)
print('No seu nome tem a palavra Silva? {}'.format('silva' in nome))
