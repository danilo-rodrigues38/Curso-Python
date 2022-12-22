# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()
print(frase)
print('Na frase aparecem {} letras A.'.format(frase.count('a')))
print('A letra A, foi encontrada pela primeira vez na posição {}.'.format(frase.find('a')+1))
print('A letra A, foi encontrada pela última vez na posição {}.'.format(frase.rfind('a')+1))
