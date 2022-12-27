def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[31mDados informados incorretos!'
                  '\nDigite somente números inteiros.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mInterrompido pelo usuário\033[m')
            return 0
        except Exception as erro:
            print(f'O problema encontrado foi {erro.__class__}')
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            n = str(input(msg)).replace(',', '.')
            num = float(n)
        except ValueError:
            print('\033[31mDados informados incorretos!'
                  '\nDigite somente números reais.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mInterrompido pelo usuário\033[m')
            return 0
        except Exception as erro:
            print(f'O problema encontrado foi {erro.__class__}')
        else:
            return num
