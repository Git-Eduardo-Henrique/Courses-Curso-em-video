"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
num_h = maior_18 = m_menor_20 = 0

while True:
    sexo = opc = " "
    print(30 * "\033[33m=-=", "\033[m")
    idade = int(input("digite a idade da pessoa: ")) 
    print(30 * "\033[33m=-=", "\033[m")

    if idade > 0 and idade < 120:
        if idade >= 18:
            maior_18 += 1

        while sexo not in "MF":
            sexo = str(input("digite o sexo da pessoa [M/F]: ")).strip().upper()[0]
            print(30 * "\033[33m=-=", "\033[m")

        if sexo == "M":
            num_h += 1
        elif sexo == "F" and idade <= 20:
            m_menor_20 += 1

        while opc not in "SN":
            opc = str(input("deseja continuar? [S/N]: ")).strip().upper()[0]
        
        if opc == "S":
            continue
        else:
            break
    else:
        print("digite uma idade valida!!")

print(30 * "\033[33m=-=", "\033[m")
print(f"pessoas com mais de 18 anos: {maior_18}")
print(f"numero de homens: {num_h}")
print(f"numero de mulheres com menos de 20 anos: {m_menor_20}")
print(30 * "\033[33m=-=", "\033[m")