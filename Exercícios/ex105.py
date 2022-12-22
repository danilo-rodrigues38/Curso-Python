# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*num, sit=False):
    """
    -> Função pra analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    maior = menor = media = soma = cont = 0
    for valor in num:
        soma += valor
        media = soma / len(num)
        if cont == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor
        cont += 1
    dicionario['total'] = len(num)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media
    if sit:
        if media < 4:
            dicionario['situação'] = 'RUIM'
        elif media > 7:
            dicionario['situação'] = 'BOA'
        else:
            dicionario['situação'] = 'RAZOÁVEL'
    return dicionario



#Programa principal
print('~' * 75)
resp = notas(5.5, 9.5, 3.5, 7, 8, 6.5, 8, 8, sit=True)
print(resp)
help(notas)
