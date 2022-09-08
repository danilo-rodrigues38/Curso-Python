# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
# será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

while True:
    nota50 = nota20 = nota10 = nota1 = 0
    print('=' * 50)
    print('BANCO CEV'.center(50))
    print('=' * 50)
    valor = int(input('Que valor você quer sacar? R$ '))
    if valor >= 50:
        nota50 = valor // 50
        valor = valor - nota50 * 50
        print(f'\nTotal de {nota50} cédulas de R$ 50')
    if valor >= 20:
        nota20 = valor // 20
        valor = valor - nota20 * 20
        print(f'Total de {nota20} cédulas de R$ 20')
    if valor >= 10:
        nota10 = valor // 10
        valor = valor - nota10 * 10
        print(f'Total de {nota10} cédulas de R$ 10')
    if valor >= 1:
        nota1 = valor // 1
        print(f'Total de {nota1} cédulas de R$ 1')
    resp = ' '
    if resp not in 'SN':
        resp = str(input('Quer sacar outro valor: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=' * 50)
print('\nObrigado por utilizar nossos serviços.\nVolte Sempre.')
