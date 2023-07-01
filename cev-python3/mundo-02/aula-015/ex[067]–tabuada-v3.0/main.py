"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor 
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    print(30 * "\033[31m=-=", "\033[m")
    num = int(input("digite um numero inteiro ( numeros negativos para parar ): "))
    print(30 * "\033[31m=-=", "\033[m")

    if num < 0:
        break
    else:
        for cont in range(1, 11):
            print(f"{num} x {cont} = {num * cont}")
