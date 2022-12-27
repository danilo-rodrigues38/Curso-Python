# Vamos criar um menu em Python, usando modularização.
#
import ex115

while True:
    ex115.menu()
    num = ex115.opção('Sua opção: ')
    if num == 1:
        ex115.relatorio(1)
    elif num == 2:
        ex115.cadastro(2)
    else:
        print('\n\033[32mObrigado! Volte Sempre!!!\033[m')
        break
