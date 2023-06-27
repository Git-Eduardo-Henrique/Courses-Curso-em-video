"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será 
formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
"""
print(30 * "\033[32m=-=", "\033[m")

seg1 = float(input("digite o primeiro segmento: "))
seg2 = float(input("digite o segundo segmento: "))
seg3 = float(input("digite o terceiro segmento: "))

print(30 * "\033[32m=-=", "\033[m")

condicao1 = seg1 + seg2 > seg3
condicao2 = seg1 + seg3 > seg2
condicao3 = seg2 + seg3 > seg1

if condicao1 and condicao2 and condicao3:
    print("Esses 3 segmentos PODEM formar um triângulo", end=" ")

    if seg1 == seg2 == seg3:
        print("equilátero")
    elif seg1 != seg2 != seg3 != seg1:
        print("escaleno")
    else:
        print("isósceles")

else:
    print("Esses 3 segmentos NÃO PODEM formar um triângulo")

print(30 * "\033[32m=-=", "\033[m")