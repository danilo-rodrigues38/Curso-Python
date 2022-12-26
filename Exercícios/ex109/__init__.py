def aumentar(vl=0, porc=0, mod=True):
    if mod:
        valor = vl + (vl * (porc / 100))
        print(f'Aumentando {porc}%, temos {moeda(valor)}')
    else:
        valor = vl + (vl * (porc / 100))
        print(f'Aumentando {porc}%, temos {valor}')


def diminuir(vl=0, porc=0, mod=True):
    if mod:
        valor = vl - (vl * (porc / 100))
        print(f'Diminuindo {porc}%, temos {moeda(valor)}')
    else:
        valor = vl - (vl * (porc / 100))
        print(f'Diminuindo {porc}%, temos {valor}')


def dobro(vl=0, mod=True):
    if mod:
        valor = vl * 2
        print(f'O dobro de {moeda(vl)} é {moeda(valor)}')
    else:
        valor = vl * 2
        print(f'O dobro de {vl} é {valor}')


def metade(vl=0, mod=True):
    if mod:
        valor = vl / 2
        print(f'A metade de {moeda(vl)} é {moeda(valor)}')
    else:
        valor = vl / 2
        print(f'A metade de {vl} é {valor}')


def moeda(vl=0, tipo='R$ '):
    return f'{tipo}{vl:.2f}'.replace('.', ',')
