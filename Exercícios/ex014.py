# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

celsious = float(input('Qual a temperatura em Graus Celsious? '))
fah = (celsious * 9 / 5) + 32
kelvin = celsious + 273.15
print('A temperatura em Graus Celsious de {} ºC. \nA temperatura em Fahrenheit corresponde a {} ºF. \nA temperatura em Kelvin corresponde a {} K.'.format(celsious, fah, kelvin))

