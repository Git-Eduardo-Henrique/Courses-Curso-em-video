"""
exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero 
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
nums = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
        "catorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    print(30 * "\033[31m=-=", "\033[m")
    num = int(input("digite um numero entre 0 e 20: "))

    if num <= 20 and num >= 0:
         break

print(30 * "\033[31m=-=", "\033[m")
print(f"voce digitou o numero: {nums[num]}")
print(30 * "\033[31m=-=", "\033[m")