# nome = str(input('Digite seu nome: '))
# if nome == 'Danilo':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal.')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
# if m >= 6:
#     print('PARABÉNS!!!')
# else:
#     print('ESTUDE MAIS!!!')
print('PARABÉNS!!!' if m >= 6 else 'ESTUDE MAIS!!!')   #Condição simplificada para IF ou ELSE

