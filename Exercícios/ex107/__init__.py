def aumentar(vl, porc=0):
    valor = vl + (vl * (porc / 100))
    print(f'Aumentando {porc}%, temos R$ {valor}')


def diminuir(vl):
    print('Diminuir')


def dobro(vl):
    valor = vl * 2
    print(f'O dobro de {vl} é {valor}')


def metade(vl):
    valor = vl / 2
    print(f'A metade de R$ {vl} é {valor}')

