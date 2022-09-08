# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO!!! Digite um número válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
print('-' * 30)
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}.')
