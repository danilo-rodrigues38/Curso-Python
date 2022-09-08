# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2) / 2
print('\nA média foi de {:.2f}.\n'.format(media))
if media < 5:
    print('Aluno \033[1:31mREPROVADO!!!\033[m')
elif media >= 5 and media < 7:
    print('Aluno em \033[33mRECUPERAÇÃO!!!\033[m')
else:
    print('Aluno \033[32mAPROVADO!!!\033[m')
