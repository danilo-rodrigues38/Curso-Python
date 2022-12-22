# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

cadastro = {'nome': str(input('Nome: ')),
            'idade': datetime.today().year - int(input('Ano de nascimento: ')),
            'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if cadastro['ctps'] != 0:
    cadastro['anopricont'] = int(input('Ano do primeiro contrato: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposent'] = (cadastro['anopricont'] - (datetime.today().year - cadastro['idade'])) + 35
print('-=' * 35)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor {v}.')
