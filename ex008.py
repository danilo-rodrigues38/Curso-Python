# Desenvolva um programa que leia uma distância em metros e mostre os valores
# relativos em outras medidas.
# Ex:
# Digite uma distância em metros: 185.72
# A distância de 85.7m corresponde a:
# 0.18572Km
# 1.8572Hm
# 18.572Dam
# 1857.2dm
# 18572.0cm
# 185720.0mm

metro = float(input('Digite uma distância em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('A distância de {}m corresponde a:'.format(metro))
print(km, 'Km')
print(hm, 'Hm')
print(dam, 'Dam')
print(dm, 'dm')
print(cm, 'cm')
print(mm, 'mm')

