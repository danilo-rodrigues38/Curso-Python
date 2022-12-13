# Elementos =  0          1        2        3           4          # Tuplas são IMUTÁVEIS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # Todas as 'Tuplas' sempre entre parenteses.

print(lanche)           # Imprime ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])        # Imprime somente 'Suco'
print(lanche[-2])       # Imprime o segundo elemento da direita para a esquerda que é 'Pizza'
print(lanche[1: 3])     # Imprime do elemento 1 que é o 'Suco' até o elemento 3, exeto o elemento 3 que é o 'Pudim' ('Suco', 'Pizza')
print(lanche[2:])       # Imprime do elemento 2 e vai até o ultimo elemento da lista.
print(lanche[:2])       # Imprime do início e vai até o elemento 2, exeto o elemento 2 que é a 'Pizza' ('Hamburguer', 'Suco')
print(lanche[-3:])      # imprime do elemento 1 e vai até o final ('Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posdição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')

print(sorted(lanche))   # Imprime em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)                # Junta as duas Tuplas
print(len(c))           # Conta quantos elementos há na Tupla
print(c.count(5))       # Conta quantas vezes aparece o número 5
print(c.index(8))       # Informa em que posição aparece o número 8 pela primeira vez
print(c.index(5, 1))    # Informa em que posição aparece o número 5 pela primeira vez iniciando pelo elemento 1

pessoa = ('Danilo', 49, 'M', 85)
del(pessoa)             # Deleta completamente a Tupla, não é possivel excluir apena um elemento
print(pessoa)
