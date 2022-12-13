'''
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')
'''

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome:-<20} tem {idade} anos e ganha R$ {salario:.2f}.')

'''
{nome:20}    O nome fica com 20 espaços.
{nome:^20}   O nome fica com 20 espaços centralizado.
{nome:-^20}  O nome fica com 20 espaços centralizado e com barras dos dois lados.
{nome:-<^20} O nome fica com 20 espaços alinhado a esquerda com as barras.
{nome:->^20} O nome fica com 20 espaços alinhado a direita com as barras.
'''
