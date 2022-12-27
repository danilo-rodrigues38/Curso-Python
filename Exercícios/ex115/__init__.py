def menu():
    print('-' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('-' * 50)
    print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2 -\033[m \033[34mCadastrar novas pessoas\033[m')
    print('\033[33m3 -\033[m \033[34mSair do Sistema\033[m')
    print('-' * 50)


def opção(msg):
    while True:
        try:
            vl = int(input(f'\033[32m{msg}\033[m'))
        except ValueError:
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mInterrompido pelo usuário.\033[m')
            break
        else:
            if 1 <= vl <= 3:
                return vl
            else:
                print('\033[31mDigite uma opção válida!\033[m')
                continue


def relatorio(n):
    print('-' * 50)
    print(f'Opção {n}'.center(50))
    print('-' * 50)


def cadastro(n):
    print('-' * 50)
    print(f'Opção {n}'.center(50))
    print('-' * 50)
