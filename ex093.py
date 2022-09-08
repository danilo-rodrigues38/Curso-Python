# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {'nome': str(input('Jogador: '))}
gols = list()
total = 0
qtdjogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, qtdjogos):
    gol = int(input(f'  Quantos gols na partida {cont}: '))
    gols.append(gol)
    total += gol
jogador['gols'] = gols[:]
jogador['total'] = total
print('-=' * 35)
print(jogador)
print('-=' * 35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 35)
print(f'O jogador {jogador["nome"]} jogou {qtdjogos} partidas.')
for k, v in enumerate(gols):
    print(f'  => Na Partida {k}, fez {v} gols.')
print(f'Foi um total de {total} gols.')
