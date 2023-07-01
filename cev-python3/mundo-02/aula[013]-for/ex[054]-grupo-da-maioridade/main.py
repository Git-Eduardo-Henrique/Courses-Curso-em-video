"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

atual = date.today().year
cont_maior = 0
cont_menor = 0

print(30 * "\033[32m=-=", "\033[m")

for num in range(1, 8):
    nasc = int(input(f"digite o ano de nascimento da {num}° pessoa: "))
    idade = atual - nasc

    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1

print(30 * "\033[32m=-=", "\033[m")
print(f"numero de pessoas com maioridade: {cont_maior}")
print(f"numero de pessoas com menos de 18 anos: {cont_menor}")
print(30 * "\033[32m=-=", "\033[m")