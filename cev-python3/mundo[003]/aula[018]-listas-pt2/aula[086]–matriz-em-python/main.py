"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo 
teclado. No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(30 * "\033[33m=-=", "\033[m")

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"digite um numero inteiro [{linha}][{coluna}]: "))

print(30 * "\033[33m=-=", "\033[m")

for linha in range(0, 3):
    print("\n")
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end=" ")

print("\n")
print(30 * "\033[33m=-=", "\033[m")