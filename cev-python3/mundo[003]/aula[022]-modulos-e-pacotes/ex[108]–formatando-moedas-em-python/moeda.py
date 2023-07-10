"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga 
mostrar os números como um valor monetário formatado.
"""

def aumentar(num = 0, por = 0):
    return num + num * (por / 100)

def diminuir(num = 0, por = 0):
    return num - num * (por / 100 )

def dobro(num = 0):
    return num * 2

def metade(num = 0):
    return num / 2


def moeda(preco = 0, moeda = "R$"):
    return f"{moeda}{preco:.2f}".replace(".", ",")