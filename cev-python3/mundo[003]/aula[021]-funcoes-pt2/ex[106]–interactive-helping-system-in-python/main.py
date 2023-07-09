"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o 
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: 
use cores.
"""
def seehelp(modulo):
    print(30 * "\033[35m=-=", "\033[m")
    print(f"{f'Analizando o modulo ou função: {modulo}':^90}")
    print(30 * "\033[35m=-=", "\033[m")
    help(modulo)

while True:
    print(30 * "\033[35m=-=", "\033[m")
    modulo = str(input("digite o nome de um modulo para ver o manual (FIM = sair): "))

    if modulo == "FIM":
        break
    else:
        seehelp(modulo=modulo)

print(30 * "\033[35m=-=", "\033[m")
print(f'{"Finalizando":^90}')
print(30 * "\033[35m=-=", "\033[m")