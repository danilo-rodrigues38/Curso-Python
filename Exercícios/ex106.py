# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''
print('\033[0;42mTeste fundo verde e letra branca.\033[m')
print('\033[1;3;32mTeste fundo normal e letra verde, negrito e itálico.\033[m')
print('\033[0;44mTeste fundo azul e letra branca.\033[m')
print('\033[7;40mTeste fundo branco e letra cinza.\033[m')
print('\033[0;41mTeste fundo vermelho e letra branca.\033[m')'''


def sysHelp(msg):
    from time import sleep
    txt = f"Acessando o manual do camando '{msg}'"
    tam = len(txt) + 4
    sleep(1)
    print('\033[0;44m~' * tam)
    print(f'{txt}'.center(tam))
    print('~' * tam)
    print('\033[m', end='')
    sleep(1)
    print(f'\033[7;40m')
    help(msg)
    print('\033[m', end='')
    sleep(1.5)


# Programa principal
while True:
    print('\033[0;42m~' * 27)
    print('SISTEMA DE AJUDA PyHELP'.center(27))
    print('~' * 27)
    print('\033[m', end='')
    msg = str(input('\033[1;3;32mFunção ou Biblioteca > \033[m')).strip()
    if msg.lower() == 'fim':
        print('\033[0;41m~' * 12)
        print('ATÉ LOGO!'.center(12))
        print('~' * 12)
        print('\033[m', end='')
        break
    else:
        sysHelp(msg)
