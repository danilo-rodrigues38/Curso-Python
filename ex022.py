# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo sem considerar os espaços.
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print()
print('Analisando o seu nome...')
print()
print('Seu nome com todas as letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}'.format(nome.lower()))

lista = nome.split()
junto = ''.join(lista)
print()
print('O nome sem considerar os espaços tem um total de {} letras'.format(len(junto)))

print()
print('O primeiro nome tem um total de {} letras.'.format(len(lista[0])))
