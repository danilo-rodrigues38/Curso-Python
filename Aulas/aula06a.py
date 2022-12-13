n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
# print('A soma entre,', n1, 'e', n2, 'é', s) - Formato antigo do Python

print('A soma entre, {} e {} é {}'.format(n1, n2, s)) # Novo formato a partir do Python 3.
