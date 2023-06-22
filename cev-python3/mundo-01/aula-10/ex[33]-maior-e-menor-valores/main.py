"""
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
maior = float
menor = float

print(30 * "\033[36m=-=", "\033[m")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o ultimo numero: "))

print(30 * "\033[36m=-=", "\033[m")

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print(f"o maior numero foi: {maior}")
print(f"o menor numero foi: {menor}")
print(30 * "\033[36m=-=", "\033[m")
