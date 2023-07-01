"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um 
atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
"""
from datetime import date

atual = date.today().year

titulo = "Confederação Nacional de Natação"

print(30 * "\033[32m=-=", "\033[m")
print(f"{titulo:^90}")

print(30 * "\033[32m=-=", "\033[m")
nasc = int(input("digite seu ano de nascimento: "))
print(30 * "\033[32m=-=", "\033[m")

idade = atual - nasc

print(f"você tem {idade} anos e pode ser considerado um atleta ", end="")
if idade <= 9:
    print("mirim")
elif idade <= 14:
    print("infantil")
elif idade <= 19:
    print("júnior")
elif idade <= 25:
    print("sênior")
else:
    print("master")

print(30 * "\033[32m=-=", "\033[m")