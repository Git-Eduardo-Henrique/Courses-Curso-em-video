"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa 
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
"""
print(30 * "\033[33m=-=", "\033[m")
peso = float(input("digite seu peso em kilos: "))
altura = float(input("digite sua altura em metros: "))
print(30 * "\033[33m=-=", "\033[m")

imc = peso / altura ** 2
print(f"seu imc é de {imc:.2f} e você está", end=" ")
if imc < 18.5:
    print("abaixo do peso!! cuidado")
elif imc < 25:
    print("com o peso ideal")
elif imc < 30:
    print("com sobrepeso")
elif imc < 40:
    print("com obesidade")
else:
    print("com obesidade mórbida!! cuidado")
    
print(30 * "\033[33m=-=", "\033[m")