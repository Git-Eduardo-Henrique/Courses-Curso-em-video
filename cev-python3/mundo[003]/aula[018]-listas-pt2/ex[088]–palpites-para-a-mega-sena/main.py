"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar 
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
composta.
"""
from random import randint
jogos = []
temp = []
cont2 = 0

print(30 * "\033[35m=-=", "\033[m")
num_jogos = int(input("numero de jogos: "))
print(30 * "\033[35m=-=", "\033[m")

for cont in range(1, num_jogos+1):
    while cont2 != 6:
        num = randint(1, 60)

        if num not in temp:
            temp.append(num)
            cont2 += 1

    cont2 = 0
    jogos.append(temp[:])
    temp.clear()

for cont3, jogo in enumerate(jogos):
    print(f"jogo {cont3+1}: {jogo}")

print(30 * "\033[35m=-=", "\033[m")