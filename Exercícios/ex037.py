# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('-' * 15)
print('BASES NUMERICAS')
print('-' * 15)
print()
num = int(input('Digite um valor inteiro: '))
print()
print("Escolha:")
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print()
esc = int(input('Qual sua escolha? '))
if esc == 1:
    print('A resposta em binário é {}.'.format(bin(num)[2:]))
elif esc == 2:
    print('A resposta em octal é {}.'.format(oct(num)[2:]))
elif esc == 3:
    print('A resposta em hexadecimal é {}.'.format(hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
