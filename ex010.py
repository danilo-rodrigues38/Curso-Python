# Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

print('Quer comprar dólares?')
dinheiro = float(input('Quanto você tem em reais? R$'))
dollar = float(input('Qual a cotação do dólar? US$'))
conversao = dinheiro / dollar

print('Com R$ {:.2f}, você pode comprar US$ {:.2f}.'. format(dinheiro, conversao))

