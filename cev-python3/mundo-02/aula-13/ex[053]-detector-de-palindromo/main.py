"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os 
espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
print(30 * "\033[31m=-=", "\033[m")
frase = str(input("digite uma frase: "))
tam_frase = len(frase)
nova_frase = ""
print(30 * "\033[31m=-=", "\033[m")

for cont in range(1, tam_frase + 1):
    nova_frase += frase[tam_frase - cont]

print(frase, nova_frase)
print(30 * "\033[31m=-=", "\033[m")