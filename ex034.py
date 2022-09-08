# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print('CALCULO DO AUMENTO SALARIAL')
print('-' * 27)
print()
sal = float(input('Digite o valor do salário atual: R$ '))
if sal > 1250:
    nsal = (sal * 10 / 100) + sal
    print('O novo salário com o aumento de 10% é de R$ {:.2f}.'.format(nsal))
else:
    nsal = (sal * 15 / 100) + sal
    print('O novo salário com o aumento de 15% é de R$ {:.2f}.'.format((nsal)))
