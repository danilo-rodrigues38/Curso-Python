# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totgasto = maismil = mbarato = 0
cont = 1
barato = ' '
print('-' * 36)
print('LOJA SUPER BARATÃO'.center(36))
print('-' * 36)
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$ '))
    totgasto += preço

# No código abaixo, na cadeia de 'if' o primeiro e o terceiro podem ser simplificados como no exemplo a seguir:
#     if cont == 1 or preço < mbarato:
#         barato = produto
#         mbarato = preço
# Enfim, essa é a forma simplificada.

    if cont == 1:
        barato = produto
        mbarato = preço
        cont +=1
    if preço >= 1000:
        maismil += 1
    if preço < mbarato:  # Excluiria-se esse if.
        barato = produto
        mbarato = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nO total da compra foi de R$ {totgasto}')
print(f'Temos {maismil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {mbarato:.2f}\n')
print('{:-^40}'.format(' FIM DO PROGRAMA '))