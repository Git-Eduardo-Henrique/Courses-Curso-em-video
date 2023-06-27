"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.
"""
print(30 * "\033[35m=-=", "\033[m")
print(f"{'10 termos da PA':^90}")
print(30 * "\033[35m=-=", "\033[m")

termo = int(input("digite o primeiro termo: "))
razao = int(input("digite a rezão: "))
decimo = termo + (10 - 1) * razao

print(30 * "\033[35m=-=", "\033[m\n")

for num in range(termo, decimo + razao, razao):
    print(num, end=" | ")

print("ACABOU! \n")
print(30 * "\033[35m=-=", "\033[m")