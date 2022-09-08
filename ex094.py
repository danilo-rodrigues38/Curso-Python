# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
mulheres = list()
medIdade = 0
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: ')).strip()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO!!! Por Favor digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados)
    del dados
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO!!! Responda apenas S ou N.')
    if resp == 'N':
        break
for c in range(0, len(pessoas)):
    medIdade += pessoas[c]['idade'] / len(pessoas)
    if pessoas[c]['sexo'] == 'F':
        mulheres.append(pessoas[c]['nome'])
print('-=' * 35)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é {medIdade:.1f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in range(0, len(mulheres)):
    print(mulheres[c], end=' ')
print()
print(f'D) Lista de pessoas que estão acima da média:')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] >= medIdade:
        for k, v in pessoas[c].items():
            print(f'    {k} = {v};', end=' ')
        print()
print('<<< ENCERRADO >>>')
