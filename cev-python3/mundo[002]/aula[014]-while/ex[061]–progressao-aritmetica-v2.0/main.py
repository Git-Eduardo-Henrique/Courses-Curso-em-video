"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while.
"""
print(30 * "\033[33m=-=", "\033[m")
print(f"{'10 termos da PA':^90}")
print(30 * "\033[33m=-=", "\033[m")

termo = int(input("digite o primeiro termo: "))
razao = int(input("digite a rezão: "))
cont = 1

print(30 * "\033[33m=-=", "\033[m\n")
while cont <= 10:
    print(f"{termo} ->", end=" ")
    termo += razao
    cont += 1


print("ACABOU! \n")
print(30 * "\033[33m=-=", "\033[m")