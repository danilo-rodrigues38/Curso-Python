# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# No código abaixo foi carregada toda a biblioteca de matemática do Python.
# import math
# co = float(input('Qual o valor do cateto oposto: '))
# ca = float(input('Qual o valor do cateto adjacente: '))
# print('A hipotenusa do triângulo retangulo é {:.2f}'.format(math.hypot(co, ca)))

# No código abaixo foi carregado somente a formula para calculo da hipotenusa.
from math import hypot
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
print('A hipotenusa do triângulo retangulo é {:.2f}'.format(hypot(co, ca)))
