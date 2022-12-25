from time import sleep
c = ('\033[m',        # 0 = Sem cores
     '\033[0;30;41',  # 1 = 30 - letra branca, 41 - fundo Vermelho
     '\033[0;30;42',  # 2 = 30 - letra branca, 42 - fundo Verde
     '\033[0;30;43',  # 3 = 30 - letra branca, 43 - fundo Amarelo
     '\033[0;30;44',  # 4 = 30 - letra branca, 44 - fundo Azul
     '\033[0;30;45',  # 5 = 30 - letra branca, 45 - fundo roxo
     '\033[7;30'      # 6 =  7 - inverte as cores, neste caso, letra preta e fundo branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'{msg}'.center(tam))
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa padrão
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!!!', 1)
