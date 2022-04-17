n1 = input("Digite um valor: ")         # Retorna sempre um valor String
n2 = str(input("Digite um valor: "))    # Força o retorno de um valor String
n3 = int(input("Digite um valor: "))    # Força o retorno de um valor inteiro
n4 = float(input("Digite um valor: "))  # Força o retorno de um valor real
n5 = bool(input("Digite um valor: "))   # Força o retorno de um valor lógico, verdadeiro ou falso 'True' or 'False'

# Para o caso do valor Boolean, caso seja digitado qualquer valor para a variável, sempre terá o retorno 'True' se não
# digitado nenhum valor, ela retornará 'False'.

print('Tipo primitivo para n1 = ', type(n1), n1)
print('Tipo primitivo para n2 = ', type(n2), n2)
print('Tipo primitivo para n3 = ', type(n3), n3)
print('Tipo primitivo para n4 = ', type(n4), n4)
print('Tipo primitivo para n5 = ', type(n5), n5)

