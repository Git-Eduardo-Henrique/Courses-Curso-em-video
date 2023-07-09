"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo 
que algum dado não tenha sido informado corretamente.
"""
def ficha(nome="", gols=0):
    if nome == "":
        nome = "<desconhecido>"

    print(30 * "\033[32m=-=", "\033[m")
    print(f"o jogador {nome} fez {gols} gols no campeonato")
    
print(30 * "\033[32m=-=", "\033[m")

nome = str(input("nome do jogador: "))
gols = str(input("gols do jogador: "))

if gols.isnumeric():
    ficha(nome=nome, gols=gols)
else:
    ficha(nome=nome)

print(30 * "\033[32m=-=", "\033[m")