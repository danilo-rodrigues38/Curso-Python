# Crie um programa que vai gerar cinco númeors aleatórios e colocar em uma TUPLA.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# minha solução para o problema
menor = maior = c = 0
from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
tpl = (n1, n2, n3, n4, n5)
print(f'Os valores sorteados foram: {tpl}')
for c in range(0, 5):
    if c == 0:
        menor = n1
        maior = n1
    if menor > tpl[c]:
        menor = tpl[c]
    if maior < tpl[c]:
        maior = tpl[c]
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')


# Solução do professor
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
