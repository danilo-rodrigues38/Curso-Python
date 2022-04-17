# Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
# na tela a sua média na disciplina.
# Ex:
# Nota 1: 4.5
# Nota 2: 8.5
# A média entre 4.5 e 8.5 é igual a 6.5

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('1ª nota {}'.format(n1))
print('2ª nota {}'.format(n2))
print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2, media))

