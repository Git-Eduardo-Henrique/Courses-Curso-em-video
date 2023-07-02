"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(30 * "\033[33m=-=", "\033[m")
print(f"numeros gerados: ", end="")

for item in nums:
    print(f"| {item}", end=" ")

print("\n")
print(30 * "\033[33m=-=", "\033[m")
print(f"menor numero: {min(nums)}")
print(f"maior numero: {max(nums)}")
print(30 * "\033[33m=-=", "\033[m")