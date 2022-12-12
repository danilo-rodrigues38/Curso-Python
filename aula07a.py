n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('')

# a sintaxe dentro das chaves referem-se as casa decimais.
print('A soma é {}, o produto é {}, a divisão é {:.2f}'.format(s, m, d), end='. ')
# no final do comando a expressão ", end='<qualquer coisa>, faz com que não haja a quebra da linha.

print('A divisão inteira é {}, a potência é {}, o resto da divaisão é {}'.format(di, e, r))

# caso queira a quebra da linha pode ser utilizado o comando, "\n".
print('A soma é {}, \no produto é {} \na divisão é {:.2f}'.format(s, m, d))