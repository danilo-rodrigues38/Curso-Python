# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

nasc = int(input('\nEm que ano você nasceu? '))
atual = date.today().year
idade = atual - nasc
print('Sua idade é {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é a MIRIM.')
elif idade <= 14:
    print('Sua categoria é a INFANTIL.')
elif idade <= 19:
    print('Sua categoria é a JÚNIOR.')
elif idade <= 25:
    print('Sua categoria é a SENIOR.')
else:
    print('Sua categoria é a MASTER.')
