"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:                   
                                                                                                                             
A) Quantos números foram digitados.                                                               
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()

while True:
    opc = " "
    print(30 * "\033[34m=-=", "\033[m")
    num = int(input("digite um numero inteiro: "))
    lista.append(num)

    while opc not in "SN":
        opc = str(input("deseja continuar? [S/N]: ")).strip().upper()[0]

    if opc == "N":
        break

print(30 * "\033[34m=-=", "\033[m")
print(f"numeros digitados: {lista}\ntotal numeros digitados: {len(lista)}")

lista.sort(reverse=True)
print(f"lista em ordem decerscente: {lista}")

if 5 in lista:
    print("o valor 5 esta na lista")
else:
    print("o valor 5 não esta na lista")

print(30 * "\033[34m=-=", "\033[m")