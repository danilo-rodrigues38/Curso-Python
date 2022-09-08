# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = list()
i = c = 0
p = str(input('Digite uma expressão: ')).strip()
print('-=' * 30)
print('A espressão digitada foi ', end='')
for cont, p in enumerate(p):
    print(p, end='')
    expressao.append(p)
    if expressao[cont] == '(':
        i += 1
    elif expressao[cont] == ')':
        c += 1
if i == c:
    print('\nA expressão está correta.')
else:
    print('\nA expressão não está correta.')
