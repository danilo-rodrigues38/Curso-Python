# Crie um programa que tenha uma TUPLA com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado','programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper():.<20}temos: ', end='')
    for v in p:
        if v in 'aeiou':
            print(v, end=' ')