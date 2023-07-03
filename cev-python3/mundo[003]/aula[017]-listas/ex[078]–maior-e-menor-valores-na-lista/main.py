"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre 
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista_valores = []

print(30 * "\033[31m=-=", "\033[m")

for cont in range(1, 6):
    valor = int(input(f"digite o {cont}° numero inteiro: "))
    lista_valores.append(valor)

maior = max(lista_valores)
menor = min(lista_valores)

print(30 * "\033[31m=-=", "\033[m\n")

print(f"maior valor digitado foi {maior} nas posições:", end=" ")
for index, item in enumerate(lista_valores):
    if item == maior:
        print(f"{index+1}°", end=" | ")
print("\n")

print(f"menor valor digitado foi {menor} nas posições:", end=" ")
for index, item in enumerate(lista_valores):
    if item == menor:
        print(f"{index+1}°", end=" | ")
print("\n")

print(30 * "\033[31m=-=", "\033[m")