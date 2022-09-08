# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual a velocidade do veículo? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado em R$ {:.2F}.\nPor ter ultrapassado o limite de 80 Km/h.'.format(multa))
else:
    print('Siga sempre assim.\nBoa Viagem!!!')
