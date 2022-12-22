# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('ALISTAMENTO MILITAR\n')
anonasc = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade < 18:
    print('Você tem {} anos, e ainda faltam {} anos para seu alistamento.'.format(idade, 18 - idade))
    print('Seu ano de alistamento será em {}.'.format(anonasc + 18))
elif idade == 18:
    print('Você tem {} anos, já está em tempo para se alistar.'.format(idade))
else:
    print('Você tem {} anos, já se passaram {} anos do seu alistamento.'.format(idade, idade - 18))
    print('Seu ano de alistamento foi em {}.'.format(anonasc + 18))
