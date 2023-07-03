"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, 
você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ("linguagem", "programacao", "python", "orientada", "objeto", "sintaxe", "variaveis", "funcoes")

print(30 * "\033[36m=-=", "\033[m")

for palavra in palavras:
    print(f"em \033[36m{palavra}\033[m temos as vogais: \033[36m", end="")

    for letra in palavra:
        if letra in "aeiou":
            if letra == "a":
                print("a", end=" | ")
            elif letra == "e":
                print("e", end=" | ")
            elif letra == "i":
                print("i", end=" | ")
            elif letra == "o":
                print("o", end=" | ")
            elif letra == "u":
                print("u", end=" | ")
    print("\033[m\n")

print(30 * "\033[36m=-=", "\033[m")
