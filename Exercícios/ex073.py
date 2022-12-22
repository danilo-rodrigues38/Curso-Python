# Crie uma TUPLA preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
# classificação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

cbf = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Internacional', 'Fluminence',
       'São Paulo', 'Flamengo', 'Botafogo', 'Santos', 'Avaí', 'Coritiba', 'América-MG', 'Bragantino',
       'Ceará SC', 'Atlético-GO', 'Goiás', 'Cuiabá', 'Juventude', 'Fortaleza')
print('-*' * 55)
print('Lista de times do Brasileirão 2022')
print(cbf)
print('-*' * 55)
print(f'Os 5 primeiros colocados são: {cbf[:5]}')
print('-*' * 55)
print(f'Os 4 últimos são: {cbf[-4:]}')
print('-*' * 55)
print('Times em ordem alfabética:')
print(sorted(cbf))
print('-*' * 55)
pos = cbf.index('Bragantino')
print(f'O Bragantino aparece na {pos + 1}ª posição')
