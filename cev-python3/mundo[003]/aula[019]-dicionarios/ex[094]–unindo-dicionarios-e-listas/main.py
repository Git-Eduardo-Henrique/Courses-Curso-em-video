"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 

A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""
soma = media = 0
pessoa = dict()
lista = list()

while True:
    opc = " "
    print(30 * "\033[35m=-=", "\033[m")
    pessoa["nome"] = str(input("digite o nome: "))

    while True:
        pessoa["sexo"] = str(input("digite o sexo (F|M): ")).strip().upper()[0]

        if pessoa["sexo"] in "FM":
            break
        else:
            print("digite um genero valido!")

    pessoa["idade"] = int(input("digite a idade: "))
    soma += pessoa["idade"]

    lista.append(pessoa.copy())

    while opc not in "SN":
        opc = str(input("deseja continuar (S/N): ")).strip().upper()[0]
    
    if opc == "N":
        break

print(30 * "\033[35m=-=", "\033[m")

for item in lista:
    print(f"nome: {item['nome']} | sexo: {item['sexo']} | idade: {item['idade']}")

print(30 * "\033[35m=-=", "\033[m")

tam = len(lista)
print(f"pessoas cadastradas: {tam}")
media = soma / tam
print(f"media de idade: {media:.0f}")

print(30 * "\033[35m=-=", "\033[m")
print("lista de mulheres:")
for item in lista:
    if item["sexo"] in "Ff":
        print(f"nome: {item['nome']} | sexo: {item['sexo']} | idade: {item['idade']}")

print(30 * "\033[35m=-=", "\033[m")
print("lista de pessoas com idade acima da media:")
for item in lista:
    if item["idade"] > media:
        print(f"nome: {item['nome']} | sexo: {item['sexo']} | idade: {item['idade']}")

print(30 * "\033[35m=-=", "\033[m")