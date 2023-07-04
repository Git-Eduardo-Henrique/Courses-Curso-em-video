"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
"""
nums = list()
pares = list()
impares = list()

while True:
    opc = " "

    print(30 * "\033[35m=-=", "\033[m")
    num = int(input("digite um numero inteiro: "))
    nums.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    while opc not in "SN":
        opc = str(input("deseja continuar? [S/N]: ")).strip().upper()[0]
    
    if opc == "N":
        break

print(30 * "\033[35m=-=", "\033[m")
print(f"numeros digitados: {nums}\nnumeros pares digitados: {pares}\nnumeros impares digitados: {impares}")
print(30 * "\033[35m=-=", "\033[m")