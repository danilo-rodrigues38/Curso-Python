# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

# Esta é a minha solução que é diferente da que o professor Gustavo Guanabara mostrou em
# aula de resolução.

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
    '''
    # Esta foi a solução do professor Gustavo Guanabara.
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['media'] = sum(num)/len(num)
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['media'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    '''
    return dicionario



#Programa principal
print('~' * 75)
resp = notas(9, 7, 8, 8, 8, sit=True)
print(resp)
#help(notas)
