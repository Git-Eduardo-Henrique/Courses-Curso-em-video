"""
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a 
mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108.
"""

def aumentar(num = 0, por = 0, format = False):
    res = num + num * (por / 100)
    if format:
        res = moeda(preco=res)

    return res

def diminuir(num = 0, por = 0, format = False):
    res = num - num * (por / 100 )
    if format:
        res = moeda(preco=res)

    return res

def dobro(num = 0, format = False):
    res = num * 2

    if format:
        res = moeda(preco=res)

    return res

def metade(num = 0, format = False):
    res = num / 2

    if format:
        res = moeda(preco=res)

    return res

def moeda(preco = 0, moeda = "R$"):
    return f"{moeda}{preco:.2f}".replace(".", ",")