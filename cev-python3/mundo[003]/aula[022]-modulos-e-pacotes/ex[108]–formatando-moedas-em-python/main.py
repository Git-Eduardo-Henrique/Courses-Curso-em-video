"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga 
mostrar os números como um valor monetário formatado.
"""

from moeda import *

print(30 * "\033[32m=-=", "\033[m")
preco = float(input("preço da compra: R$"))
porcentagem = int(input("porcentagem para aumento e diminuição: "))

formatado = moeda(preco=preco)

print(30 * "\033[32m=-=", "\033[m")

print(f"o dobro de {formatado}: {moeda(preco=dobro(num=preco))}\n"
      f"a metade de {formatado}: {moeda(preco=metade(num=preco))}\n"
      f"aumentando {porcentagem}%: {moeda(preco=aumentar(num=preco, por=porcentagem))}\n"
      f"diminuindo {porcentagem}%: {moeda(preco=diminuir(num=preco, por=porcentagem))}")

print(30 * "\033[32m=-=", "\033[m")