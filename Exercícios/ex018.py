# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
graus = float(input('Digite um ângulo: '))
angulo = math.radians(graus)
print('O seno é {:.2f} rad.'.format(math.sin(angulo)))
print('O cosseno é {:.2f} rad.'.format(math.cos(angulo)))
print('A tangente é {:.2f} rad.'.format(math.tan(angulo)))

