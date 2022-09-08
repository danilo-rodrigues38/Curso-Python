# Conceito de empacotar parâmetros
# Criando tuplas
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim!')


# Programa principal

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(4, 4, 7, 6, 2)