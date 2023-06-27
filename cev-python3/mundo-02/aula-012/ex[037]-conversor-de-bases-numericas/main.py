"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
print(30 * "\033[34m=-=", "\033[m")
num = int(input("Digite um numero inteiro: "))
print(30 * "\033[34m=-=", "\033[m")

titulo = "Opções de conversão"
print(f"{titulo:^90}")
print(30 * "\033[34m=-=", "\033[m")

print("[ 1 ] = BINARIO\n[ 2 ] = OCTAL\n[ 3 ] = HEXADECIMAL")
print(30 * "\033[34m=-=", "\033[m")

opc = int(input("sua opção: "))
print(30 * "\033[34m=-=", "\033[m")
if opc == 1:
    print(f"numero {num} em binario: {bin(num)}")
elif opc == 2:
    print(f"numero {num} em octal: {oct(num)}")
elif opc == 3:
    print(f"numero {num} em hexadecimal: {hex(num)}")
else:
    print("opção invalida!!!")

print(30 * "\033[34m=-=", "\033[m")