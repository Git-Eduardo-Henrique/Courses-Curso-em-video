"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

atual = date.today().year

print(30 * "\033[36m=-=", "\033[m")
nasc = int(input("digite o ano você nasceu: "))
print(30 * "\033[36m=-=", "\033[m")

idade = atual - nasc
alistamento = nasc + 18

print(f"você nasceu em {nasc} e tem {idade} anos em {atual}")
if idade > 18:
    print(f"você já deveira ter se alistado ha {idade - 18} anos\nseu alistamento foi em {alistamento}")
elif idade < 18:
    print(f"você vai ter que se alistar em {18 - idade} anos\nseu alistamento vai ser em {alistamento}")
else:
    print(f"você vai tem que se alistar neste ano de {atual}")

print(30 * "\033[36m=-=", "\033[m")
