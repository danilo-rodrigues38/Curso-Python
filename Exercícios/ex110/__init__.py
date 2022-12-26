def aumentar(vl=0, porc=0, mod=True):
    """
    -->Aumenta um valor recebido conforme a porcentagem.
    :param vl: Valor Recebido.
    :param porc: Porcentagem recebida.
    :param mod: Parâmetro par retorno da função monetária.
    :return: Valor mostrando ou não a função monetária
    """
    valor = vl + (vl * (porc / 100))
    return valor if not mod else moeda(valor)


def diminuir(vl=0, porc=0, mod=True):
    """
        -->Diminui um valor recebido conforme a porcentagem.
        :param vl: Valor Recebido.
        :param porc: Porcentagem recebida.
        :param mod: Parâmetro par retorno da função monetária.
        :return: Valor mostrando ou não a função monetária
        """
    valor = vl - (vl * (porc / 100))
    return valor if not mod else moeda(valor)


def dobro(vl=0, mod=True):
    """
    -->Dobra um valor recebido.
    :param vl: Valor recebido.
    :param mod: Parâmetro par retorno da função monetária.
    :return: Valor mostrando ou não a função monetária.
    """
    valor = vl * 2
    return valor if not mod else moeda(valor)


def metade(vl=0, mod=True):
    """
    -->Divide pela metade um valor recebido.
    :param vl: Valor recebido.
    :param mod: Parâmetro par retorno da função monetária.
    :return: Valor mostrando ou não a função monetária.
    """
    valor = vl / 2
    return valor if not mod else moeda(valor)


def moeda(vl=0, tipo='R$ '):
    """
    -->Função para conversão em moeda local.
    :param vl: Valor recebido.
    :param tipo: Tipo de moeda local, padrão "R$".
    :return: Retorna um valor monetário local "ex: R$ 200,00".
    """
    return f'{tipo}{vl:.2f}'.replace('.', ',')


def resumo(vl=0, up=10, down=5):
    """
    -->Retorna um resumo com valoes monetários.
    :param vl: Valor recebido.
    :param up: Porcentagem para aumento de um valor.
    :param down: Porcentagem para redução de um valor.
    :return: Função sem retorno.
    """
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(vl)}')
    print(f'Dobro do preço: \t{dobro(vl)}')
    print(f'Metade do preço: \t{metade(vl)}')
    print(f'{up}% de aumento: \t{aumentar(vl, up)}')
    print(f'{down}% de redução: \t{diminuir(vl, down)}')
    print('-' * 30)
