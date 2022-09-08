'''
dados = dict()
dados = {'nome': 'pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)
'''
filme = {'titulo': 'Star War',
         'ano': 1977,
         'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = [{'titulo': 'Star War',
             'ano': 1977,
             'diretor': 'George Lucas'},
            {'titulo': 'Avengers',
             'ano': 2012,
             'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix',
             'ano': 1999,
             'diretor': 'Wachauski'}]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])
