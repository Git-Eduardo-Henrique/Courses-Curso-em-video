"""
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
print(30 * "\033[36m=-=", "\033[m")
print("preparando para os fogos...")
print(30 * "\033[36m=-=", "\033[m")

for num in range(10, 0, -1):
    sleep(1)

    print(str(num).zfill(2))

print(30 * "\033[36m=-=", "\033[m")
print("ESTOUROU POW POW ******")
print(30 * "\033[36m=-=", "\033[m")