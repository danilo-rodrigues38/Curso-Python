# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

s = 0
v = 0
for cont in range(1, 501):
    if cont % 2 == 1:
        if cont % 3 == 0:
            v += 1
            s += cont
print('A soma de todos os {} números ímpares, divisiveis por 3 é {}.'.format(v, s))
