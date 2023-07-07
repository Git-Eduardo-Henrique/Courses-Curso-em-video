"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, 
fim e passo. Seu programa tem que realizar três contagens através da função criada:     

a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada
"""
from time import sleep

def contador(ini = 0, fim = 0, passo = 1, temp = 0):
    for cont in range(ini, fim+passo, passo):
        sleep(temp)
        print(f"-> {cont}", end=" ")
    print()

print(30 * "\033[33m=-=", "\033[m")
print(f"{'contagem programada de 1 a 10, passo 1':^90}")
contador(ini=1, fim=10, passo=1)

print(30 * "\033[33m=-=", "\033[m")
print(f"{'contagem programada de 10 a 0, passo 2':^90}")
contador(ini=10, fim=0, passo=-2)

print(30 * "\033[33m=-=", "\033[m")
inicio = int(input("começo da contagem: "))
final = int(input("fim da contagem: "))
passo = int(input("de quanto em quanto: "))
tempo = float(input("tempo de intervalo a contagem: "))

print(30 * "\033[33m=-=", "\033[m")
print(f"{f'sua contagem de {inicio} a {final}, passo {passo}':^90}")
contador(ini=inicio, fim=final, passo=passo, temp=tempo)
print(30 * "\033[33m=-=", "\033[m")