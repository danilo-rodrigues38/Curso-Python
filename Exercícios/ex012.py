# Crie um programa que leia o preço de um produto, calcule e mostre o seu
# PREÇO PROMOCIONAL, com 5% de desconto.

preco = float(input('Digite o valor do produto: R$ '))
desconto = preco - (preco * 0.05)
print('O novo valor promocional é de R$ {:.2f}'.format(desconto))

