"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial

print(30 * "\033[32m=-=", "\033[m")
num = int(input("digite um numero para saber seu fatorial: "))
fatorial = factorial(num)
print(30 * "\033[32m=-=", "\033[m")

print(f"{num}! = ", end="")

while num > 0:
    print(f"{num}", end=" ")

    if num > 1:
        print("x", end=" ")
    else:
        print("=", end=" ")

    num -= 1

print(f"{fatorial}")
print(30 * "\033[32m=-=", "\033[m")