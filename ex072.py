# Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso de zero até vinte.
# Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

# Esta foi a minha solução para o programa
num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    if 0 <= resp <= 20:  # if resp >= 0 and resp <= 20:
        print(f'Você digitou o número {num[resp]}.')
        break
    else:
        print('Tente novamente. ', end='')

# Esta é a solução do professor
'''
while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    if 0 <= resp <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {num[resp]}.')
'''
