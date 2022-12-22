# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
totpar = soma3c = maival2c = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]:'))
        if num % 2 == 0:
            totpar += num
        matriz[l].append(num)
    if matriz[l][2] >= 0:
        soma3c += matriz[l][2]
print('-=' * 35)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for n in matriz[1]:
    if n > maival2c:
        maival2c = n
print('-=' * 35)
print(f'A soma de todos os valora pares é {totpar}.')
print(f'A Soma dos valores da terceira coluna é {soma3c}.')
print(f'O maior valor da segunda linha é {maival2c}.')
