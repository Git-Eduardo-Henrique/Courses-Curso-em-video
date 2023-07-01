"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
esc = " "

from random import randint
print(30 * "\033[32m=-=", "\033[m")
print(f"{'par ou impar':^90}")
print(30 * "\033[32m=-=", "\033[m")

while True:
    pc = randint(0, 10)
    num = int(input("digite um numero inteiro (de 0 a 10): "))

    if num < 0 or num > 10:
        print("numero invalido!!!! tente novamente")
    else:
        soma = num + pc
        while esc not in "PI":
            esc = input("qual vc escolhe? [ P = par, I = impar ]: ").strip().upper()[0]
            print(30 * "\033[32m=-=", "\033[m")

        if esc == "P": # se deu par
            print("Você escolheu par, pc escolheu impar")
            if soma % 2 == 0:
                print(f"soma deu {soma} portanto deu par!! Voce ganhou")
            else:
                print(f"soma deu {soma} portanto deu impar!! Voce perdeu")
                break
        else: # se deu impar
            print("Você escolheu impar, pc escolheu par")
            if soma % 2 == 0:
                print(f"soma deu {soma} portanto deu par!! Voce perdeu")
                break
            else:
                print(f"soma deu {soma} portanto deu impar!! Voce ganhou")
            print(30 * "\033[32m=-=", "\033[m")

print(30 * "\033[32m=-=", "\033[m")
