# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('\033[31m')
print('-' * 21)
print('TABOADA'.center(21))
print('-' * 21)
print('\033[m')
n = int(input('Digite um número: '))
for cont in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, cont, n * cont))
