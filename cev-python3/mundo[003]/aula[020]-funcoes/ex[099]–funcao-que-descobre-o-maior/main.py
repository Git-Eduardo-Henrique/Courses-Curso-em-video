"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def maior(nums = list()):
    maior_num = 0

    for item in nums:
        if item > maior_num:
            maior_num = item
    
    return maior_num

nums = list()

while True:
    opc = " "

    print(30 * "\033[34m=-=", "\033[m")
    num = int(input("digite um numero inteiro: "))
    nums.append(num)

    while opc not in "SN":
        opc = str(input("deseja continuar (S/N)? ")).strip().upper()[0]

    if opc == "N":
        break

print(30 * "\033[34m=-=", "\033[m")
print(f"voce digitou: {nums}\no maior valor foi: {maior(nums=nums)}")
print(30 * "\033[34m=-=", "\033[m")