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
def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: recebe o primeiro valor
    :param b: recebe o segundo valor
    :param c: recebe o terceiro valor
    :return:  sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}.')


soma(3, 2, 5)
soma(8, 4)
soma()
soma(b=4, c=5)



# Escopo de variáveis
def teste():
    x = 8  # "x" é uma variável local, ou seja, funciona somente na função teste
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


# Programa principal
n = 2  # "n" é uma variável global
print(f'No programa principal, n vale {n}.')
teste()
#print(f'No programa princial, x vale {x}.')  # neste caso, o "x" não funcionará, por ser uma variável local.



# Retorno de valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}.')
