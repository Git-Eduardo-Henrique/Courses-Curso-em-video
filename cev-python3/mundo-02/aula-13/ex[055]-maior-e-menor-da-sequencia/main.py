"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor 
peso lidos.
"""
maior_peso = 0
menor_peso = 0
print(30 * "\033[33m=-=", "\033[m")

for num in range(1, 6):
    peso = float(input(f"digite o peso da {num}° pessoa (kg): "))

    if num == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        
        if peso < menor_peso:
            menor_peso = peso

print(30 * "\033[33m=-=", "\033[m")   
print(f"e maior peso foi de {maior_peso:.1f}kg e o menor foi de {menor_peso:.1f}kg") 
print(30 * "\033[33m=-=", "\033[m")