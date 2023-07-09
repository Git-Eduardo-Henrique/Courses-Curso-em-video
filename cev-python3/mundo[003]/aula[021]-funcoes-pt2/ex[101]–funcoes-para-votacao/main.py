"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO 
nas eleições.
"""
from datetime import date

atual = date.today().year

def voto(idade = 0):
    voto = " "

    if idade >= 18:
        voto = "Obrigatório"
    elif idade >= 16:
        voto = "Opcional"
    else:
        voto = "Negado"
    
    return voto
    
print(30 * "\033[36m=-=", "\033[m")
nasc = int(input("digite o ano de nascimento: "))

idade = atual - nasc

print(f"você tem {idade} anos e seu voto é {voto(idade=idade)}")
print(30 * "\033[36m=-=", "\033[m")