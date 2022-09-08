# Desempacotamento no Python
def soma(*val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')


# programa principal
soma(5, 2)
soma(2, 9, 4)
soma(2, 2, 0, 5, 1, 9, 7, 3)
