def aumentar(vl=0, porc=0):
    valor = vl + (vl * (porc / 100))
    print(f'Aumentando {porc}%, temos {moeda(valor)}')


def diminuir(vl=0, porc=0):
    valor = vl + (vl * (porc / 100))
    print(f'Diminuindo {porc}%, temos R$ {moeda(valor)}')


def dobro(vl=0):
    valor = vl * 2
    print(f'O dobro de {moeda(vl)} é {moeda(valor)}')


def metade(vl=0):
    valor = vl / 2
    print(f'A metade de {moeda(vl)} é {moeda(valor)}')


def moeda(vl=0, tipo='R$ '):
    return f'{tipo}{vl:.2f}'.replace('.', ',')
