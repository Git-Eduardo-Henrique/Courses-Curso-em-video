"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista 
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
de cada aluno individualmente.
"""
lista = []
media = 0

while True:
    opc = " "
    print(30 * "\033[36m=-=", "\033[m")
    nome = str(input("digite o nome do aluno: "))
    nota1 = float(input("digite a primeira nota: ")) 
    nota2 = float(input("digite a segunda nota: ")) 

    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    while opc not in "SN":
        print(30 * "\033[36m=-=", "\033[m")
        opc = str(input("deseja continuar? ")).strip().upper()[0]
        
    if opc == "N":
        break

print(30 * "\033[36m=-=", "\033[m")
print(f"{'Numero':^29}|{'nome':^29}|{'media':^30}")

for cont, item in enumerate(lista):
    print(f"{cont+1:^29}|{item[0]:^29}|{item[2]:^29}")

while True:
    print(30 * "\033[36m=-=", "\033[m")
    aluno = int(input("digite o numero do aluno (999 = sair): "))

    if aluno == 999:
        break
    if aluno <= len(lista):
        print(f"aluno: {lista[aluno - 1][0]} | nota 1: {lista[aluno - 1][1][0]} | nota 2: {lista[aluno - 1][1][1]}")
    else:
        print("aluno não cadastrado!!")

print(30 * "\033[36m=-=", "\033[m")