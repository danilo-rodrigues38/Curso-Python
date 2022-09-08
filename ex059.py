# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = int(input('\nPrimeiro valor: '))
n2 = int(input('Segundo valor: '))
resp = 0
while resp != 5:
    print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        ''')
    resp = int(input('>>>>> Qual é a sua opção? '))
    if resp == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2 , n1 + n2))
        print('=-' * 15)
    elif resp == 2:
        print('A resultado de {} x {} é {}.'.format(n1, n2, n1 * n2))
        print('-=' * 15)
    elif resp == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n1))
            print('-*' * 15)
        elif n1 < n2:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n2))
            print('-*' * 15)
        elif n1 == n2:
            print('Os números são iguais.')
            print('*-' * 15)
    elif resp == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif resp > 5:
        print('Opção inválida. Tente novamente.')
    else:
        print('Finalizando', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')