"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
No final, mostre:   

A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.
"""
lista = []
temp = []
cont_pessoas = maior = menor = 0

while True:
    opc = " "
    print(30 * "\033[31m=-=", "\033[m")
    nome = str(input("digite o nome: "))
    peso = float(input("digite o peso (kg): "))

    temp.append(nome)
    temp.append(peso)

    if len(lista) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    
    lista.append(temp[:])
    temp.clear()
   
    while opc not in "SN":
        opc = str(input("deseja continuar? ")).strip().upper()[0]

    if opc == "N":
        break

print(30 * "\033[31m=-=", "\033[m\n")

print(f"pessoas cadastradas: {int(len(lista))}\n")

print(f"maior peso foi de {maior}kg de ", end="")
for pessoa in lista:
    if pessoa[1] == maior:
        print(pessoa[0], end=" ")
print("\n")
print(f"menor peso foi de {menor}kg de ", end="")
for pessoa in lista:
    if pessoa[1] == menor:
        print(pessoa[0], end=" | ")

print("\n")
print(30 * "\033[31m=-=", "\033[m")
