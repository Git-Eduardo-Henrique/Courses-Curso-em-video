"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado 
ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(num = 0, show = False):
    fato = num
    for cont in range(num, 0, -1):

        if cont != num:
            fato *= cont

        if show:
            if cont != 1:
                print(f"{cont} x", end=" ")
            else:
                print(f"{cont} =", end=" ")

    print(f"{fato}")

print(30 * "\033[31m=-=", "\033[m")
num = int(input("digite um numero para ver seu fatorial: "))
opc = " "
while opc not in "SN":
    opc = str(input("deseja mostrar o processo? (S/N): ")).strip().upper()[0]

print(30 * "\033[31m=-=", "\033[m")

if opc == "S":
    fatorial(num, True)
else:
    fatorial(num)

print(30 * "\033[31m=-=", "\033[m")