"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o 
vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    "jogador-1": randint(1, 6),
    "jogador-2": randint(1, 6),
    "jogador-3": randint(1, 6),
    "jogador-4": randint(1, 6),
    }

# itemgetter = organiza pela chave ou item 0 = chave 1 = item
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(30 * "\033[32m=-=", "\033[m")
print(f'{"valores sortedos":^90}')
print(30 * "\033[32m=-=", "\033[m")

for chave, item in jogadores.items():
    sleep(0.5)
    print(f"{chave} tirou {item} no dado")

print(30 * "\033[32m=-=", "\033[m")
print(f"{'ranking':^90}")
print(30 * "\033[32m=-=", "\033[m")

for cont, item in enumerate(ranking):
    sleep(0.25)
    print(f"{cont+1}° lugar - {item[0]} que tirou {item[1]}")

print(30 * "\033[32m=-=", "\033[m")