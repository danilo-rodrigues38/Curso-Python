# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
n = 1
soma = media = maior = menor = total = 0
while resp in 'Ss':
    n = int(input('Digite um número inteiro: '))
    total += 1
    soma += n
    media = soma / total
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('~' * 35)
print('Você digitou {} números e a média foi {}.'.format(total, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
