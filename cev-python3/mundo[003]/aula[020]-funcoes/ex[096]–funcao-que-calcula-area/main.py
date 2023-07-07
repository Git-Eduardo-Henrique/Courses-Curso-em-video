"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
retangular (largura e comprimento) e mostre a área do terreno.
"""
def area(larg = 0, comp = 0):
    return larg * comp

print(30 * "\033[31m=-=", "\033[m")
largura = float(input("digite a largura do terreno (m): "))
comprimento = float(input("digite o comprimento do terreno (m): "))

print(30 * "\033[31m=-=", "\033[m")
print(f"a area é de: {area(larg=largura, comp=comprimento)}m²")
print(30 * "\033[31m=-=", "\033[m")