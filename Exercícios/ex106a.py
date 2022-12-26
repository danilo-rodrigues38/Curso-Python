from time import sleep
c = ('\033[m',        # 0 = Sem cores
     '\033[0;41m',  # 1 = 41 - fundo Vermelho com lerta branca
     '\033[0;42m',  # 2 = 42 - fundo Verde com lerta branca
     '\033[0;43m',  # 3 = 43 - fundo Amarelo com lerta branca
     '\033[0;44m',  # 4 = 44 - fundo Azul com lerta branca
     '\033[0;45m',  # 5 = 45 - fundo roxo com lerta branca
     '\033[7;40m'   # 6 =  7 - inverte as cores, neste caso, letra preta e fundo branco
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


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!!!', 1)
