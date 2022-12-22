# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1:31m-\033[m' * 19)
print('\033[1:31mEMPRÉSTIMO BANCÁRIO\033[m')
print('\033[1:31m-\033[m' * 19)
print()
casa = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o salário do proponente? R$ '))
anos = float(input('Em quantos anos deseja pagar o imóvel? '))
prestcasa = casa / (anos * 12)
mensal = salario * 30 / 100
print()
print('O valor da prestação mensal é de R$ {:.2f} mensais.'.format(prestcasa))
print()
if prestcasa > mensal:
    print('Com o salário de \033[31mR$ {:.2f}\033[m, o valor máximo da prestação não pode ultrapassar o limite de \033[31mR$ {:.2f}\033[m mensais.'.format(salario, mensal))
    print('\033[1:31mEMPRÉSTIMO NEGADO.\033[m')
else:
    print('Com o salário de \033[32mR$ {:.2f}\033[m, voçê está dentro do limite de \033[31m30%\033[m que é de \033[32mR$ {:.2f}\033[m mensais.'.format(salario, mensal))
    print('\033[1:32mPARABÉNS EMPRÉSTIMO APROVADO\033[M')
