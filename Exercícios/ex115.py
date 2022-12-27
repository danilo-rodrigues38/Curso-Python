# Vamos criar um menu em Python, usando modularização.
# Vamos ver como fazer acesso a arquivos usando o Python.

import ex115
from time import sleep
arq = 'cursoemvideo.txt'

if not ex115.arquivoExiste(arq):
    ex115.criarArquivo(arq)

while True:
    ex115.menu()
    num = ex115.opção('Sua opção: ')
    if num == 1:
        ex115.relatorio(arq)
    elif num == 2:
        ex115.cadastro(arq)
    else:
        print('\n\033[32mObrigado! Volte Sempre!!!\033[m')
        break
    sleep(2)
