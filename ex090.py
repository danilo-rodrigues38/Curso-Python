# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

escola = dict()
escola['nome'] = str(input('Nome: ')).strip()
escola['media'] = float(input(f'Média de {escola["nome"]}: '))
if escola['media'] < 4:
    escola['situacao'] = 'REPROVADO'
elif escola['media'] < 7:
    escola['situacao'] = 'RECUPERAÇÂO'
else:
    escola['situacao'] = 'APROVADO'
print('-=' * 35)
for k, v in escola.items():
    print(f'  - {k} é igual a {v}')
print(escola)
