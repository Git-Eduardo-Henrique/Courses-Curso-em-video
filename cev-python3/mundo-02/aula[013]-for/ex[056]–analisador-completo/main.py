"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
from datetime import date

atual = date.today().year
idade_m_velho = 0
nome_m_velho = 0
cont_mulher = 0
media = 0

print(30 * "\033[34m=-=", "\033[m")

for num in range(1, 5):
    nome = str(input(f"digite o nome da {num}° pessoa: "))
    idade = int(input(f"digite a idade da {num}° pessoa: "))
    sexo = str(input(f"digite o sexo da {num}° pessoa(F/M): ")).upper()

    media += idade 

    print(30 * "\033[34m=-=", "\033[m")
    if sexo == "M" and idade > idade_m_velho:
        idade_m_velho = idade
        nome_m_velho = nome
    elif sexo == "F" and idade < 20:
            cont_mulher += 1
            
media /= 4

print(f"media de idade: {media} anos")
print(f"{nome_m_velho} é o homem mais velho e tem {idade_m_velho} anos")
print(f"numero de mulheres com menos de 20 anos: {cont_mulher}")
print(30 * "\033[34m=-=", "\033[m")