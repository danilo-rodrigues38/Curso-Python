# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo;
# qual é o nome do homem mais velho;
# quantas mulheres têm menos de 20 anos.

totmulher = 0
totidade = 0
imvelho = 0
media = 0
for cont in range(1,5):
    print('----- {}ª PESSOA -----'.format(cont))
    nome = str(input('Nome: '.format(cont))).strip()
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    idade = int(input('Idade: '))
    totidade += idade
    media = totidade / 4
    if sexo == 'F' and idade < 20:
        totmulher += 1
    elif sexo == 'M' and idade > imvelho:
        imvelho = idade
        hmvelho = nome
print('A média de idade do grupo é de {} anos.'.format(media))
print('O nome do homem mais velho é {} com {} anos.'.format(hmvelho, imvelho))
print('O total de mulheres com menos de 20 anos é {}.'.format(totmulher))
