"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando 
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual 
foi a soma entre eles (desconsiderando o flag).
"""
soma = cont_nums = num = 0

print(30 * "\033[36m=-=", "\033[m")

while num != 999:
    num = int(input("digite um numero inteiro (999 para parar): "))
    print(30 * "\033[36m=-=", "\033[m")

    if num != 999:
        soma += num
        cont_nums += 1

print(f"total numeros digitados: {cont_nums}")
print(f"a soma de todos os numeros deu: {soma}")
print(30 * "\033[36m=-=", "\033[m")