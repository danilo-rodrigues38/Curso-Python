# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número.
    """
    fat = 1
    for cont in range(num, 0, -1):
        fat *= cont
        if show:
            print(f'{cont} ', end='')
            if cont == 1:
                print('= ', end='')
            else:
                print('* ', end='')
    return fat


print('-' * 30)
numero = int(input('Fatorial de: '))
mostra = str(input('Quer ver a sequencia do fatorial? [S/N] ')).strip().lower()[0]
if mostra == 's':
    ver = True
else:
    ver = False
resp = fatorial(numero, ver)
print(resp)
