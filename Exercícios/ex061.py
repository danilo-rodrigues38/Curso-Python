# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

# Minha resolução do exercício.
print('\033[32m')
print('*-' * 25)
print('Progressão Aritimética'.center(50))
print('-*' * 25)
print('\033[m')

primeiro = int(input('Primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} →'.format(termo), end='')
    termo += razao
    cont += 1
print('ACABOU')

