# Crie um pacote chamado utilidadesCeV que tenha dois pacotes internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 110 para o pacote moeda e mantenha  tudo
# funcionando.

import ex111.moeda
valor = float(input('Digite um valor: R$ '))
ex111.moeda.resumo(valor, 20, 12)
