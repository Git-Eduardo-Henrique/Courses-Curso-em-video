"""
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
aumento = float
print(30 * "\033[31m=-=", "\033[m")
salario = float(input("digite seu sálario: R$"))
print(30 * "\033[31m=-=", "\033[m")

if salario > 1250:
    aumento = salario + (salario * 0.1)
else:
    aumento = salario + (salario * 0.15)

print(f"seu antigo salario de R${salario:.2f} com aumento é de: R${aumento:.2f}")
print(30 * "\033[31m=-=", "\033[m")
