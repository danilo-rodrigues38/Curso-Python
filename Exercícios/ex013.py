# Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
# seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$ '))
novosalario = salario + (salario * 0.15)
print('O novo salário, com 15% de aumento é de R$ {:.2f}.'.format(novosalario))

