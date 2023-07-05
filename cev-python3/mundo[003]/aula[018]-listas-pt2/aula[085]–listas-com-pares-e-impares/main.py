"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em 
ordem crescente.
"""
nums = [[], []]
num = 0

for cont in range(1, 8):
    print(30 * "\033[32m=-=", "\033[m")
    num = int(input(f"digite o {cont}° numero inteiro: "))

    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

print(30 * "\033[32m=-=", "\033[m")
print(f"numeros pares: {sorted(nums[0])}\nnumeros impares: {sorted(nums[1])}")
print(30 * "\033[32m=-=", "\033[m")