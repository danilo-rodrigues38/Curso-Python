pessoas = list()

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas.append(dados[:])
print(pessoas)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)          # imprime as lista e suas sub-listas
print(pessoas[0])       # imprime a sub-lista 0
print(pessoas[0][0])    # imprime o item 0 da sub-lista 0, no caso aqui 'Pedro'
print(pessoas[1][1])    # imprime o item 1 da sub-lista 1, no caso aqui 19
print(pessoas[2][0])    # imprime o item 0 da sub-lista 2, no caso aqui 'João'

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])     # muito cuidado para não esquecer o [:]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])     # muito cuidado para não esquecer o [:]
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade.')
