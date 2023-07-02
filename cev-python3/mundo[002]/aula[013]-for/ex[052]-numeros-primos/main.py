"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print(30 * "\033[36m=-=", "\033[m")
num = int(input("digite um numero inteiro: "))
print(30 * "\033[36m=-=", "\033[m")
cont_divi = 0

for cont in range(1, num + 1):
    if num % cont == 0:
        cont_divi += 1

print(f"o numero {num} foi divisivel {cont_divi} vezes", end=" ")

if cont_divi == 2:
    print("e por isso ele é um numero primo")
else:
    print("e por isso ele não é um numero primo")
    
print(30 * "\033[36m=-=", "\033[m")