"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), 
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
from moeda import *

print(30 * "\033[31m=-=", "\033[m")
preco = float(input("preço da compra: R$"))
porcentagem = int(input("porcentagem para aumento e diminuição: "))

print(30 * "\033[31m=-=", "\033[m")
print(f"o dobro de R${preco:.2f}: R${dobro(num=preco):.2f}\n"
      f"a metade de R${preco:.2f}: R${metade(num=preco):.2f}\n"
      f"aumentando {porcentagem}%: R${aumentar(num=preco, por=porcentagem):.2f}\n"
      f"diminuindo {porcentagem}%: R${diminuir(num=preco, por=porcentagem):.2f}")
print(30 * "\033[31m=-=", "\033[m")