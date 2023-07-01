"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se 
o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
maior_1000 = gasto = menor = 0
nome_barato = opc = " "

print(30 * "\033[34m=-=", "\033[m")
print(f"{'mercadinho do seu zé'}")
print(30 * "\033[34m=-=", "\033[m")

while True:
    opc = " "

    nome = str(input("digite o nome do produto: "))
    preco = float(input("digite o valor do produto: R$"))
    print(30 * "\033[34m=-=", "\033[m")

    gasto += preco

    if preco > 1000:
        maior_1000 += 1

    if menor == 0:
        menor = preco
        nome_barato = nome
    else:
        if preco < menor:
            menor = preco
            nome_barato = nome

    while opc not in "SN":
        opc = str(input("deseja continuar? [S/N]: ")).strip().upper()[0]
        print(30 * "\033[34m=-=", "\033[m")
    
    if opc == "S":
        continue
    else:
        break

print(f"total do compra: R${gasto:.2f}\nprodutos com preço maior que R$1000: {maior_1000}")
print(f"o produto mais barato foi o {nome_barato} que custou R${menor:.2f}")
print(30 * "\033[34m=-=", "\033[m")