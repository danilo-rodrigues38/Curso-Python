def tabuada(num):
    print('~' * 16)
    print(f'TABUADA do {num}'.center(16))
    print('~' * 16)
    for c in range(1, 11):
        print(f'  {c:2} x {num} = {num * c:2}')


# Programa principal
n = int(input('Olá! Quer ver a tabuada de que número? '))
tabuada(n)
