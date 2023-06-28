"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

print(30 * "\033[31m=-=", "\033[m")
print(f"{'super calculadora 2000':^90}")
print(30 * "\033[31m=-=", "\033[m")
valor_1 = float(input("digite o primeiro valor: "))
valor_2 = float(input("digite o segundo valor: "))

while True:
    sleep(1)
    print(30 * "\033[31m=-=", "\033[m")
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    print(30 * "\033[31m=-=", "\033[m")

    opc = int(input("sua opção: "))
    print(30 * "\033[31m=-=", "\033[m")

    if opc == 1:
        print(f"{valor_1} + {valor_2} = {valor_1 + valor_2}")
    elif opc == 2:
        print(f"{valor_1} x {valor_2} = {valor_1 * valor_2}")
    elif opc == 3:
        if valor_1 > valor_2:
            print(f"o valor {valor_1} é o maior valor")
        else:
            print(f"o valor {valor_2} é o maior valor")
    elif opc == 4:
        valor_1 = float(input("digite o primeiro valor: "))
        valor_2 = float(input("digite o segundo valor: "))
    elif opc == 5:
        print("Saindo... ")
        print(30 * "\033[31m=-=", "\033[m")
        break
    else:
        print("operação invalida!!!")
