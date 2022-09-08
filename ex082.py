# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
# conteúdo das três listas geradas.

lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor ou, digite 999 para sair: '))
    if n == 999:
        break
    else:
        if n in lista:
            print('O número digitado já está na lista. Digite outro.')
        else:
            lista.append(n)
            if n % 2 == 0:
                pares.append(n)
            else:
                impares.append(n)
lista.sort()
pares.sort()
impares.sort()
print(f'Você digitou {len(lista)} números.')
print(f'A lista digitada foi {lista}.')
print(f'Os valores pares digitados foram {pares}.')
print(f'Os valores ímpares digitados foram {impares}.')
