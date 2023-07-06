"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o 
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

atual = date.today().year

pessoa = dict()

print(30 * "\033[33m=-=", "\033[m")
pessoa["nome"] = str(input("digite o nome: "))
nasc = int(input("digite o ano de nascimento: "))
pessoa["idade"] = atual - nasc
pessoa["carteira"] = int(input("digite a carteira de trabalho (0 = sem): "))

if pessoa["carteira"] != 0:
    pessoa["contratação"] = int(input("digite o ano de contratação: "))
    pessoa["aposentadoria"] = pessoa["idade"] + ((pessoa["contratação"] + 35) - atual)
    pessoa["salario"] = float(input("digite o salario: R$"))

print(30 * "\033[33m=-=", "\033[m")

for chave, item in pessoa.items():
    print(f"{chave} = {item}")

print(30 * "\033[33m=-=", "\033[m")