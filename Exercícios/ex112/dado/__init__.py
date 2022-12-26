def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0:31mERRO: "{valor}" não é um preço válido!!!\033[m')
        else:
            return float(valor)
            break
