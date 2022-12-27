def cabeçalho(msg):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)


def menu():
    cabeçalho('MENU PRINCIPAL')
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


def relatorio(msg):
    try:
        a = open(msg, 'rt')
    except:
        print('\n\033[31mErro ao ler arquivo!')
    else:
        cabeçalho('Pessoas Cadastradas')
        print(a.readlines())


def cadastro(msg):
    try:
        a = open(msg, 'at')
    except:
        print('\n\033[31mErro ao ler arquivo!')
    else:
        cabeçalho('NOVO CADASTRO')


def arquivoExiste(msg):
    try:
        a = open(msg, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(msg):
    try:
        a = open(msg, 'wt+')
        a.close()
    except:
        print('\n\n\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\n\n\033[32mAquivo {msg} criado com sucesso!!!\033[m'.center(50))
