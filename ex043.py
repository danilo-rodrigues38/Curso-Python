# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print('Calculo do IMC')
print('-' * 14)
peso = float(input('\nDigite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('\nO Seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print('Você está no PESO IDEAL. Parabéns!')
elif imc < 30:
    print('Você está com SOBREPESO.')
elif imc < 40:
    print('Você está com OBESIDADE. Atenção!!!')
else:
    print('Você está com OBESIDADE MÓBIDA. Procure a ajuda de um proficional URGENTE!!!')
