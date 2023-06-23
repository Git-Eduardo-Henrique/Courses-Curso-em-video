"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem 
pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
cont_pares = 0
print(30 * "\033[34m=-=", "\033[m")

for cont in range(1, 7):
    num = int(input(f"digite o {cont}° numero inteiro: "))
    if num % 2 == 0:
        soma += num
        cont_pares += 1

print(30 * "\033[34m=-=", "\033[m")
print(f"você digitou {cont_pares} numeros pares e a soma foi: {soma}")
print(30 * "\033[34m=-=", "\033[m")