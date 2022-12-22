# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

km = int(input('Qual a distância da viagem em Km? '))
if km <= 200:
    val = km * 0.5
    print('O valor da viagem é de R$ {:.2f}.'.format(val))
else:
    val = ((km - 200) * 0.45) + 100
    print('O valor da viagem é de R$ {:.2f}.'.format(val))
