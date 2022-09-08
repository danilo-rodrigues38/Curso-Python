# Crie um programa que tenha uma TUPLA única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)

for l in range(0, len(lista)):
    if l % 2 == 0:
        print(f'{lista[l]:.<31}', end='')
    else:
        print(f'R$ {lista[l]:>6.2f}')
