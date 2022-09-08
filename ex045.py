# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('{:=^35}'.format(' JOKENPÔ '))
print('''
Vamos lá! Escolha:
PEDRA, PAPEL OU TESOURA
''')
esch = str(input('Digite sua escolha: ')).strip().upper()
escc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('\nJO... ', end='')
sleep(1)
print('KE... ', end='')
sleep(1)
print('PÔ!!! \n')
sleep(1)
if escc == 'PEDRA' and esch == 'PEDRA':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('EMPATE!!! JOGUE NOVAMENTE.')
elif escc == 'PEDRA' and esch == 'PAPEL':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('VOCÊ GANHOU!!! JOGUE NOVAMENTE.')
elif escc == 'PEDRA' and esch == 'TESOURA':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('COMPUTADOR GANHOU!!! JOGUE NOVAMENTE.')
elif escc == 'PAPEL' and esch == 'PEDRA':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('COMPUTADOR GANHOU!!! JOGUE NOVAMENTE.')
elif escc == 'PAPEL' and esch == 'PAPEL':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('EMPATE!!! JOGUE NOVAMENTE.')
elif escc == 'PAPEL' and esch == 'TESOURA':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('VOCÊ GANHOU!!! JOGUE NOVAMENTE.')
elif escc == 'TESOURA' and esch == 'PEDRA':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('VOCÊ GANHOU!!! JOGUE NOVAMENTE.')
elif escc == 'TESOURA' and esch == 'PAPEL':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('COMPUTADOR GANHOU!!! JOGUE NOVAMENTE.')
elif escc == 'TESOURA' and esch == 'TESOURA':
    print('Computador escolheu {} e você escolheu {}.'.format(escc, esch))
    print('EMPATE!!! JOGUE NOVAMENTE.')
else:
    print('Para não exibir esta mensagem novamente,\ndigite somente PEDRA, PAPEL OU TESOURA!')
print('\nObrigado por jogar comigo!!!')
