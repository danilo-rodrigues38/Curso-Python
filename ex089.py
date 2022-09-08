# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

from time import sleep
alunos = list()
aluno = list()
while True:
    aluno.append(str(input('Nome: ')).strip())
    aluno.append(float(input('Primeira nota: ')))
    aluno.append(float(input('Segunda nota: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    alunos.append(aluno[:])
    aluno.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO!!! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 35)
print(f'{"Nº":<4}', f'{"NOME":<15}', f'{"MÉDIA":>7}')
for c in range(0, len(alunos)):
    print(f'{c:<4}', f'{alunos[c][0]:<15}', f'{alunos[c][3]:>7.2f}')
while True:
    print('-=' * 35)
    rsp = int(input('Mostrar notas de qual aluno? (999 interronpe) '))
    if rsp == 999:
        break
    elif rsp > len(alunos) - 1:
        print('Aluno inexistente!!! Digite novamente.')
    else:
        print(f'Notas do {alunos[rsp][0]} são: {alunos[rsp][1]} e {alunos[rsp][2]}')
print('FINALIZANDO', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print('  Volte Sempre!!!  '.center(35, '-'))
