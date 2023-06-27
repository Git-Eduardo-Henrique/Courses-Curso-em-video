"""
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
print(30 * "\033[31m=-=", "\033[m")
print(f"{'Numeros pares de 1 a 50':^90}")
print(30 * "\033[31m=-=", "\033[m")

for num in range(2, 51, 2):
    print(num, end=" | ")

print(f"\n {'ACABOU!!!':^90}")
print(30 * "\033[31m=-=", "\033[m")