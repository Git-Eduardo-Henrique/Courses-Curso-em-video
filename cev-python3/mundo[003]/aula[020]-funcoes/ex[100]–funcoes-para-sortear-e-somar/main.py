"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda 
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint

def sorteia():
    lista = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]

    return lista

def somapar(lista = list()):
    soma = 0

    for item in lista:
        if item % 2 == 0:
            soma += item

    return soma

lista = sorteia()
soma = somapar(lista=lista)

print(30 * "\033[35m=-=", "\033[m")
print(f"valores sorteados: {lista}\nsoma de todos os valores pares: {soma}")
print(30 * "\033[35m=-=", "\033[m")