# Quando um código se torna muito repetitivo, utilizamos funções para não termos que escrever
# varias vezes o mesmo código, para isso, utilizamos a função "def".
def linha():
    print('-' * 30)


# Programa principal
linha()
print('Curso em Vídeo')
linha()
print('Aprendendo Python')
linha()
print('Danilo Rodrigues de Oliveira')
linha()



# Podemos também criar a função para passar somente o texto e a função retorna o título.
def título(msg):
    print('-' * 30)
    print(f'{msg}'.center(30))
    print('-' * 30)


# Programa principal
título('Curso em Vídeo')
título('Aprendendo Python')
título("Danilo R Oliveira")



# Passagem de parâmetros de dois valores "A e B"
def soma(a, b):
    s = a + b
    print(f'A = {a} e B = {b}.')
    print(f'A soma entre {a} e {b} é igual a {s}.')


# Programa principal
soma(4, 5)
soma(a=7, b=2)
soma(b=5, a=3)



# Desempacotamento no Python utiliza-se o "*", onde é passado vários valores e o Python trabalha com eles.
# Os valores passados pelo Python são sempre passados por referência e são armazenados em uma Tupla.
def soma(* val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')


# programa principal
soma(5, 2)
soma(2, 9, 4)
soma(2, 2, 0, 5, 1, 9, 7, 3)
