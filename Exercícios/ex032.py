# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date # Importando somente o módulo para analisar o ano atual

print('Vamos descobrir se o ano é ou não BISSEXTO.')
ano = int(input('Digite o ano, para analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year  # Pega o ano do sistema
if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
