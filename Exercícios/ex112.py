# Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(), mas com uma
# validação de dados para aceitar apenas valores que seja monetários.

import ex112.moeda
import ex112.dado

valor = ex112.dado.leiaDinheiro('Digite um valor: R$ ')
ex112.moeda.resumo(valor, 20, 12)
