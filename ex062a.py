primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('ACABOU')
    mais = int(input('Quantos termos você que ver a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))