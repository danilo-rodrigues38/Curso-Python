# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Minha solução para o programa.
from random import randint
cont = 0
print('=-' * 25)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(50))
while True:
    print('=-' * 25)
    computador = randint(0, 10)
    numero = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = computador + numero
    if soma % 2 == 0 and escolha in 'Pp':
        print('-' * 55)
        print(f'Você jogou {numero} e o computados {computador}. Total de {soma} DEU PAR.')
        print('-' * 55)
        print('Você VENCEU!\nVamos jogar novamente...')
        cont += 1
    if soma % 2 == 1 and escolha in 'Ii':
        print('-' * 55)
        print(f'Você jogou {numero} e o computados {computador}. Total de {soma} DEU ÍMPAR.')
        print('-' * 55)
        print('Você VENCEU!\nVamos jogar novamente...')
        cont += 1
    if soma % 2 == 0 and escolha in 'Ii':
        print('-' * 55)
        print(f'Você jogou {numero} e o computados {computador}. Total de {soma} DEU PAR.')
        print('-' * 55)
        print('Você PERDEU!')
        break
    if soma % 2 == 1 and escolha in 'Pp':
        print('-' * 55)
        print(f'Você jogou {numero} e o computados {computador}. Total de {soma} DEU ÍMPAR.')
        print('-' * 55)
        print('Você PERDEU!')
        break
print('=-' * 25)
if cont > 0:
    print(f'GAME OVER!!! Você venceu {cont} vezes.')
else:
    print('CAME OVER!!! Você não venceu nenhuma partida.')

'''
# Solucção do programa pelo professor
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I} ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes.')'''