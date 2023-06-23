"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora 
utilizando um laço for.
"""
print(30 * "\033[33m=-=", "\033[m")
tabu = int(input("Digite um numero para ver sua tabuada: "))
print(30 * "\033[33m=-=", "\033[m")

for cont in range(1, 11):
    print(f"{tabu} x {str(cont).zfill(2)} = {tabu * cont}")

print(30 * "\033[33m=-=", "\033[m")