print('====== DESAFIO 004 ======')
n = input('Digite qualquer coisa: ')
print('')
print(n)
print('O tipo primitivo é:', type(n))
print('')
print('O que foi digitado é número? ', n.isnumeric())
print('O que foi digitado é alfabético?', n.isalpha())
print('O que foi digitado é alfanumérico?', n.isalnum())
print('O que foi digitado é decimal?', n.isdecimal())
print('O que foi digitado está tudo em maiúscula?', n.isupper())
print('O que foi digitado está tudo em minúscula?', n.islower())

