"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
print(30 * "\033[34m=-=", "\033[m")
num1 = int(input("digite um numero inteiro: "))
num2 = int(input("digite um outro numero inteiro: "))
num3 = int(input("digite um outro numero inteiro: "))
num4 = int(input("digite um outro numero inteiro: "))
print(30 * "\033[34m=-=", "\033[m")

nums = (num1, num2, num3, num4)

print("numeros pares: ", end="")
for item in nums:
    if item % 2 == 0:
        print(f"{item},", end=" ")

print(f"\nquantidade de numeros 9: {nums.count(9)}")

if 3 in nums:
    print(f"posição do valor 3: {nums.index(3)+1}")
else:
    print("não foi digitado o valor 3")
print(30 * "\033[34m=-=", "\033[m")