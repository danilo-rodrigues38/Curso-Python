# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

# from random import randint

# print('''\nSou seu computador...
# Acabei de pensar em um número entre 0 e 10.
# Será que você consegue adivinhar qual foi?\n''')
'''
n1 = int(input('Qual o seu palpite? '))
n2 = randint(0, 10)
ppt = 0

while n1 != n2:
    if n1 > n2:
        print('Menos... Tente novamente.')
    else:
        print('Mais... Tente novamente.')
    n1 = int(input('Qual o seu palpite? '))
    ppt += 1
print('\nVocê acetou no {}º palpite.'.format(ppt + 1))
print('O número que eu pensei foi {}.'.format(n2))
'''

# Abaixo o código de resolução do exercício do Gustavo Guanabara, detalhe na logica!!!

from random import randint   # Importa somente a função desejada.
computador = randint(0, 10)  # Aqui o computador escolhe um número do intervalo.
print('''\nSou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?\n''')
acertou = False     # Aqui ele define a varialvel como falsa.
palpite = 0         # Aqui ele define um valor inicial para o palpite.
while not acertou:  # Aqui se faz o questionamento lógico, ou seja, enquanto não for verdadeiro TRUE.
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:  # Aqui se o jogador digitou o número correto, é atribuido verdadeiro a
        acertou = True         # variavel 'acertou'
    else:
        if jogador < computador:    # Se o jogador digitou um valor abaixo do escolhido pelo computador.
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:  # Se o jogador digitou um valor acima do escolhido pelo computador.
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))
