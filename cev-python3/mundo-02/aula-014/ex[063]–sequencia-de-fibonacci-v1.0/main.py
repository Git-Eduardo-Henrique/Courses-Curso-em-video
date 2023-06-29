"""
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros 
elementos de uma Sequência de Fibonacci. Exemplo:
0 - 1 - 1 - 2 - 3 - 5 - 8
"""
t1 = 0
t2 = 1
cont = 3

print(30 * "\033[35m=-=", "\033[m")
num = int(input("quantos termos você deseja ver: "))
print(30 * "\033[35m=-=", "\033[m")

print(f"{t1} -> {t2}", end=" ")

while cont <= num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f"-> {t3}", end=" ")
    cont += 1

print("\n", 30 * "\033[35m=-=", "\033[m")