"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma 
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista = []
print(30 * "\033[33m=-=", "\033[m")
for cont in range(1, 6):
    valor = int(input("digite um numero: "))

    if cont == 1 or valor > lista[-1]:
        lista.append(valor)
        print("adiciona a ultima posição da lista")
    else:
        for pos, item in enumerate(lista):
            if valor <= item:
                lista.insert(pos, valor)
                print(f"adicionado a {pos+1}° posição")
                break
            
    print(30 * "\033[33m=-=", "\033[m")

print(lista)
print(30 * "\033[33m=-=", "\033[m")