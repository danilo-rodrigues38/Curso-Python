# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('\033[32m')
print('*-' * 25)
print('Progressão Aritimética'.center(50))
print('-*' * 25)
print('\033[m')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
i = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while i <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        i += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
