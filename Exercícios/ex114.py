import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\n\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print('\n\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
