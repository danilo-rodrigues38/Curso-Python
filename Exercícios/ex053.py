# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA, [qtdstr::-1]
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# qtdstr = len(junto)
# reverso = junto[qtdstr::-1]
reverso = junto[::-1]  # Retirar esta linha se for fazer uso do 'for'.
print('\nO inverso de {} é {}.\n'.format(junto, reverso))  # Caso faça uso do 'for', colocar esta linha após o 'for'.
'''
    Uma outra maneira de fazer a junção fazendo uso do 'for'.
for cont in range(len(junto) -1, -1, -1):
    reverso += junto[cont]
'''
if junto == reverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
