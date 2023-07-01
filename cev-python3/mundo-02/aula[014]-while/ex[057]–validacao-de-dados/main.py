"""
xercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str
while True:
    print(30 * "\033[35m=-=", "\033[m")
    sexo = str(input("informe seu sexo (F/M): ")).upper()
    print(30 * "\033[35m=-=", "\033[m")

    if sexo == "M" or sexo == "F":
        break
    else:
        print("sexo invalido!!!!")

if sexo == "M":
    print("voce selecionou o sexo masculino")
else:
    print("voce selecionou o sexo feminino")
print(30 * "\033[35m=-=", "\033[m")