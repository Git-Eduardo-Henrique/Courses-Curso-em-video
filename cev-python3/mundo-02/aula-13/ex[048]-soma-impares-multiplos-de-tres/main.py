"""
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se 
encontram no intervalo de 1 até 500.
"""
soma = 0
cont_num = 0
print(30 * "\033[32m=-=", "\033[m")

for cont in range(1, 501, 2):
    if cont % 3 == 0:
        soma += cont
        cont_num += 1

print(f"entre 1 e 500 há \033[32m{cont_num}\033[m numeros divisiveis por 3 e soma de todos foi: \033[32m{soma}\033[m")
print(30 * "\033[32m=-=", "\033[m")