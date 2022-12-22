# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(data):
    idade = date.today().year - data
    print(f'Com {idade} anos e ', end='')
    if idade < 16:
        return 'NEGADO'
    elif idade >= 18 and idade <= 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'


# Programa principal
nasc = int(input('Em que ano você nasceu: '))
id = voto(nasc)
print(f'o voto é {id}')
