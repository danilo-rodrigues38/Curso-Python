# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


print('-' * 30)
nomeJogador = str(input('Nome do jogador: '))
numGols = str(input('Números de gols: '))
if numGols.isnumeric():
    numGols = int(numGols)
else:
    numGols = 0
if nomeJogador.strip() == '':
    ficha(gol=numGols)
else:
    ficha(nomeJogador, numGols)
