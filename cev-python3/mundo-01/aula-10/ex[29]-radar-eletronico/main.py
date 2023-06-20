"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma 
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

print(30 * "\033[32m=-=", "\033[m")
velocidade = float(input("Digite a velocidade atual do carro (em km/h): "))
print(30 * "\033[32m=-=", "\033[m")

kms_acima = velocidade - 80

if velocidade > 80:
    multa = kms_acima * 7
    print(f"MULTADO!!! velocidade acima de 80km/h, multa de R${multa:.2f}")
else:
    print("velocidade abaixo do limite, pode passar")

print(30 * "\033[32m=-=", "\033[m")