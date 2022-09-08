def tabuada(num):
    print('~' * 15)
    print(f'TABUADA do {num}'.center(15))
    print('~' * 15)
    for c in range(1, 11):
        print(f'  {c:2} x {num} = {num * c:2}')


# Programa principal
n = int(input('Olá! Quer ver a tabuada de que número? '))
tabuada(n)
