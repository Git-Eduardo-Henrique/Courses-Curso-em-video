"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os 
espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
print(30 * "\033[31m=-=", "\033[m")

frase = str(input("digite uma frase: ")).split(" ")
nova_frase = ''.join(frase)
reverso_frase = nova_frase[::-1]

print(30 * "\033[31m=-=", "\033[m")

if nova_frase == reverso_frase:
    print("esta frase é um palindromo!")
else:
    print("esta frase não é um palindromo!")

print(30 * "\033[31m=-=", "\033[m")