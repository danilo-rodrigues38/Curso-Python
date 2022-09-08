'''
# TUPLA
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2])
# lanche[3] = 'sorvete'  As Tuplas são imutáveis.


lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
lanche.append('bolacha')                # Insere um item ao final da lista
lanche.insert(0, 'Cachorro-Quente')     # Insere um item na posição zero da lista
lanche.insert(2, 'Refrigerante')        # Insere um item na posição dois da lista
del lanche[3]                           # Deleta o item na posição três da lista
lanche.pop(3)                           # Também usado para apagar um item na posição três
lanche.remove('Pudim')                  # Remove o item 'Pudim' da lista
if 'pizza' in lanche:                   # Somente vai remover um item se ele estiver na lista
    lanche.remove('Pizza')
print(lanche, '\n')

valores = list(range(4, 11))
print(valores, '\n')

valores = [8, 2, 5, 4, 9, 3, 0]         # Criando lista com valores aleatórios
print(valores)
valores.sort()                          # Comando para organizar em ordem crescente
print(valores)
valores.sort(reverse=True)              # Comando para organizar em ordem decrescente
print(valores)
print(len(valores))                     # Quantos elementos há na lista

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista.')
'''
a = [2, 3, 4, 7]
b = a[:]                # Se colocar somente 'b = a' o Python faz uma ligação entre as duas listas
b[2] = 8                # por esse motivo é necessário incluir '[:]' para se fazer uma cópia da lista.
print(f'Lista A: {a}')
print(f'Lista B: {b}')
