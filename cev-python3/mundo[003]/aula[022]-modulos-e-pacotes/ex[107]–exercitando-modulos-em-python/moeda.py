"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), 
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

def aumentar(num = 0, por = 0):
    return num + num * (por / 100)

def diminuir(num = 0, por = 0):
    return num - num * (por / 100 )

def dobro(num = 0):
    return num * 2

def metade(num = 0):
    return num / 2
