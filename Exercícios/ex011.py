# Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

comprimento = float(input('Digite o comprimento da parede: '))
altura = float(input('Digite a altura da parede: '))
area = comprimento * altura
qtdtinta = area / 2
print('A área da parede a ser pintada é de {:.2f}m²'.format(area))
print('A quantidade de tinta que será necessária é de {:.2f} litros de tinta.'. format(qtdtinta))

