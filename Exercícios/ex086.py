# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite um valor para [{c}, {i}]: '))
        matriz[c].append(num)
print('-=' * 35)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    if i == 2:   # na solução do professor não necessita desta linha
        print()  # esta linha se alinha com o for.
