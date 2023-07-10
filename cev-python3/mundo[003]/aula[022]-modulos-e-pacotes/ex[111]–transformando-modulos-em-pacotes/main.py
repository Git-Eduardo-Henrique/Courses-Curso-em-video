"""
Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""

from utilidadescev.moeda.init import *

print(30 * "\033[35m=-=", "\033[m")
preco = float(input("preço da compra: R$"))
porcentagem = int(input("porcentagem para aumento e diminuição: "))
print(30 * "\033[35m=-=", "\033[m")

resumo(preco=preco, taxa=porcentagem, format=True)
print(30 * "\033[35m=-=", "\033[m")