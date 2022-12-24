import util
# É uma boa prática, quando os módulos ou pacotes que são criados pelo programador, serem importados com  a  expressão
# acima, pois, caso haja outros módulos ou pacotes sendo importados no código, podem haver incompatibilidade, por essa
# razão não é uma boa prática utilizar o comando "from util import fatorial, dobro, triplo", principalmente se o  pro-
# gramador utilizar os nomes das funções, módulos ou pacotes no idioma inglês.

num = int(input('\nDigite um valor: '))
fat = util.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {util.dobro(num)}')
print(f'O triplo de {num} é {util.triplo(num)}')


# No código abaixo, será mostrado a utilização do pacote "Uteis" de exemplo criado.
# Quando se é criado um pacote no PyCharm, a própria IDE cria um arquivo "__init__.py" automaticamente, e nesse arqui-
# vo é inserido as funções que serão utilizadas, diferentemente dos módulos, que é criado somente um arquivo.
from Uteis import numeros

number = int(input('\nDigite um valor: '))
print(f'O fatorial de {num} é {numeros.fatorial(number)}')
print(f'O dobro de {num} é {numeros.dobro(number)}')
print(f'O triplo de {num} é {numeros.triplo(number)}')
