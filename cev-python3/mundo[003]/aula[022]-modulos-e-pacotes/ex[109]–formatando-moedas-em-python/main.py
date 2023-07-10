"""
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a 
mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108.
"""

from moeda import *

print(30 * "\033[33m=-=", "\033[m")
preco = float(input("preço da compra: R$"))
porcentagem = int(input("porcentagem para aumento e diminuição: "))

formatado = moeda(preco=preco)

print(30 * "\033[33m=-=", "\033[m")

print(f"o dobro de {formatado}: {dobro(num=preco, format=True)}\n"
      f"a metade de {formatado}: {metade(num=preco, format=True)}\n"
      f"aumentando {porcentagem}%: {aumentar(num=preco, por=porcentagem, format=True)}\n"
      f"diminuindo {porcentagem}%: {diminuir(num=preco, por=porcentagem, format=True)}")

print(30 * "\033[33m=-=", "\033[m")