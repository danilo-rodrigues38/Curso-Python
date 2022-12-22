# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numero = list()
resp = 's'
while True:
    num = (int(input('Digite um valor: ')))
    if num in numero:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numero.append(num)
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
numero.sort()
print(f'Você digitou os valores {numero}')
