# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Este foi o método que encontrei para resolução do problema.
pessoas = list()
auxiliar = list()
totpes = 0
while True:
    auxiliar.append(str(input('Nome: ')))
    auxiliar.append(float(input('Peso: ')))
    pessoas.append(auxiliar[:])
    auxiliar.clear()
    totpes += 1
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas cadastradas foram: {totpes}')
print('As pessoas mais pesadas são: ', end='')
for p in pessoas:
    if p[1] >= 100:
        print(p[0], end=' ')
print('\nAs pessoas mais leves são: ', end='')
for p in pessoas:
    if p[1] <= 65:
        print(p[0], end=' ')
# resolução do professor

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 35)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
