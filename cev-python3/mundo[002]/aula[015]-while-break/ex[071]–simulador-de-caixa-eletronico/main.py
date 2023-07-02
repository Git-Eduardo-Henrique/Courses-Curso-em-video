"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao 
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão 
entregues. 

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print(30 * "\033[35m=-=", "\033[m")
valor = int(input("valor a sacar ( inteiro ): R$"))
print(30 * "\033[35m=-=", "\033[m")

ced = 200
totced = 0

while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"total de {totced} cedulas de R${ced}")
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1

        totced = 0
        if valor == 0:
            break

print(30 * "\033[35m=-=", "\033[m")