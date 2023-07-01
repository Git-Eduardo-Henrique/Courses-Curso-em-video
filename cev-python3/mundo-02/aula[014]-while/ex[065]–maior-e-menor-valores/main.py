"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a 
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele 
quer ou não continuar a digitar valores.
"""
soma = cont = media = maior = menor =  0

while True:
    print(30 * "\033[31m=-=", "\033[m")
    num = int(input("digite um numero inteiro: "))
    print(30 * "\033[31m=-=", "\033[m")
    soma += num
    cont += 1

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    opc = str(input("deseja continuar? (S/N): ")).strip().upper()[0]
    if opc == "S":
        continue
    elif opc == "N":
        break
    else:
        print("opção invalida!!!!")

media = soma / cont
print(30 * "\033[31m=-=", "\033[m")
print(f"o maior valor foi {maior} e o menor foi {menor}")
print(f"voce digitou {cont} numeros\na media de todos os numeros é {media:.2f}")
print(30 * "\033[31m=-=", "\033[m")
