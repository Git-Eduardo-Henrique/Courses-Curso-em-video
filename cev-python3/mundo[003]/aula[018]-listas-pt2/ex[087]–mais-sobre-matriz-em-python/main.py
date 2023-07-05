"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:             

A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_3 = maior = 0

print(30 * "\033[34m=-=", "\033[m")

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"digite um numero inteiro [{linha}][{coluna}]: "))

print(30 * "\033[34m=-=", "\033[m")

for linha in range(0, 3):
    print("\n")

    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end=" ")

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]

        if coluna == 2:
            soma_3 += matriz[linha][coluna]

print("\n")
print(30 * "\033[34m=-=", "\033[m")

print(f"soma de todos os numeros pares: {soma_pares}\nsoma dos valores da 3 coluna: {soma_3}"
      f"\nmaior valor da segunda linha: {maior}")

print(30 * "\033[34m=-=", "\033[m")