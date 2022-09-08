# Interactive Help - usar a função help(), mostra na tela todos as informações da função
help(print)
help(input)

# docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem.
    :param f: fim da contagem.
    :param p: passo da contagem.
    :return: sem retorno.
    """
    cont = i
    while cont <= f:
        print(f'{cont}', end='... ')
        cont += p
    print('FIM')


contador(2, 10, 2)
help(contador)



# Parametros opcionais
def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: recebe o primeiro valor
    :param b: recebe o segundo valor
    :param c: recebe o terceiro valor
    :return:  sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)
somar()
somar(b=4, c=5)


# Escopo de variáveis
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


n = 2
print(f'No programa principal, n vale {n}.')
teste()
#print(f'Na função teste, x vale {x}.')  neste caso o X não funciona por ser local

# Retorno de valores
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {3}.')
