# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    tot = int(input(f'Quantas paritdas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na {c + 1}ª partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 70)
print(f'{"Cod":>4}', f'{"Nome":<25}', f'{"Gols":<25}', f'{"Total"}')
for k, v in enumerate(time):
    print(f'{k:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<25}', end=' ')
    print()
print('-' * 70)
while True:
    busca = int(input('Mostar dados de qual jogador? (999 para parar) '))
    print()
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!!! Não existe jogador com o código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 70)
print('<<< VOLTE SEMPRE >>>')
