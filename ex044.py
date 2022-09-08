# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('''\033[1:31m
----------------------
CONDIÇÕES DE PAGAMENTO
----------------------
\033[m''')
print('''\033[33m
Escolha a opção de pagamento:
1 - à vista, dinheiro/cheque: 10% de desconto
2 - à vista, no cartão de débito/crédito: 5% de desconto
3 - parcelado em 2x no cartão: preço normal
4 - em 3x ou mais no cartão: 20% de acrécimo
\033[m''')
opcao = int(input('Escolha uma opção: '))
preco = float(input('Qual o valor do produto? R$ '))
if opcao == 1:
    valor = preco - (preco * 10 / 100)
    print('O novo valor do produto que era R$ {:.2f}, com o desconto de 10%, fica em R$ {:.2f}.'.format(preco, valor))
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
    print('O novo valor do produto que era R$ {:.2f}, com o desconto de 5%, fica em R$ {:.2f}.'.format(preco, valor))
elif opcao == 3:
    valor = preco / 2
    print('Você escolheu pagar em duas parcelas iguais no valor de R$ {:.2f}.'.format(valor))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? Máximo de 24 vezes. '))
    valor = (preco * 20 / 100) + preco
    mensal = valor / parcelas
    print('O valor total do produto é de R$ {:.2f}, que serão pagas em {} parcelas mensais no valor de R$ {:.2f}.'.format(valor, parcelas, mensal))
else:
    print('Você digitou a opção errada. Tente novamente.')

