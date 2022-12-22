# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('\033[32m')
print('PROGRESSÃO ARITIMÉTICA'.center(50))
print('*' * 50)
print('\033[m')

primeiro = int(input('Digite o primeiro termo de uma P.A.: '))
termos = int(input('Digite a quantidade de termos na P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))
enezimo = primeiro + (termos - 1) * razao
for cont in range(primeiro, enezimo + razao, razao):
    print('{}'.format(cont), end=' → ')
print('ACABOU')
print('*' * 50)
print(enezimo)
