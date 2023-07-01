"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint

itens = ("pedra","papel","tesoura")
bot = randint(0, 2)

print(30 * "\033[35m=-=", "\033[m")
print(f"{'Jokenpô':^90}")
print(30 * "\033[35m=-=", "\033[m")
print("[ 0 ] = pedra\n[ 1 ] = papel\n[ 2 ] = tesoura")
print(30 * "\033[35m=-=", "\033[m")

opc = int(input("sua opção: "))
print(30 * "\033[35m=-=", "\033[m")
print(f"você escolheu: {itens[opc]} | bot escolheu: {itens[bot]}")
if opc == 0:
    if bot == 0:
        print("EMPATE!!!")
    elif bot == 1:
        print("O BOT VENCEU!!")
    else:
        print("O PLAYER VENCEU!!!")
elif opc == 1:
    if bot == 0:
        print("O PLAYER VENCEU!!!")
    elif bot == 1:
        print("EMPATE!!!")
    else:
        print("O BOT VENCEU!!")
elif opc == 2:
    if bot == 0:
        print("O BOT VENCEU!!")
    elif bot == 1:
        print("O PLAYER VENCEU!!!")
    else:
        print("EMPATE!!!")
else:
    print("numero invalido!")
print(30 * "\033[35m=-=", "\033[m")