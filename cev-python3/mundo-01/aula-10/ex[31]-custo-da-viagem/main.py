"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
print(30 * "\033[34m=-=", "\033[m")
distancia = float(input("distancia da viagem ( km ): "))
print(30 * "\033[34m=-=", "\033[m")

if distancia <= 200:
    preco_viagem = distancia * 0.5
else:
    preco_viagem = distancia * 0.45

print(f"preço da viagem: R${preco_viagem:.2f}")
print(30 * "\033[34m=-=", "\033[m")
