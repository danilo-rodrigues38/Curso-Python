# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def titulo():
    print('-' * 35)
    print(f'{"Calculo de área do terreno":^35}')
    print('-' * 35)
    print()


def area(l, c):
    print(f'Um terreno com dimenções {l} x {c}, tem uma área total de {l * c}m².')


# Programa princial.

titulo()
print('Digite as dimenções do terreno:')
larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)
