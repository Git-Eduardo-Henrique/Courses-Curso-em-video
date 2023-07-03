"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma 
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente.
"""
lista = list()

while True:
    opc = " "

    print(30 * "\033[32m=-=", "\033[m")
    valor = int(input("digite um numero inteiro: "))

    if valor not in lista:
        lista.append(valor)
    else:
        print("valor já cadastrado!!! ")

    while opc not in "SN":
        opc = str(input("deseja continuar? [S/N]: ")).strip().upper()[0]

    if opc == "S":
        continue
    else:
        break

print(30 * "\033[32m=-=", "\033[m")
print(f"voce digitou: {sorted(lista)}")
print(30 * "\033[32m=-=", "\033[m")