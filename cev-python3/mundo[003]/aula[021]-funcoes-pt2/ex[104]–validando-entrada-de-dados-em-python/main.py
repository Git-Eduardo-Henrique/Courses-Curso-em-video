"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um n: ')
"""
def leiaint(perg = ""):
    while True:
        print(30 * "\033[33m=-=", "\033[m")
        num = input(f"{perg}")

        if num.isnumeric():
            break
        else:
            print(30 * "\033[33m=-=", "\033[m")
            print("DIGITE UM NUMERO!!!")

    print(30 * "\033[33m=-=", "\033[m")
    print(f"você digitou o numero {num}")
    print(30 * "\033[33m=-=", "\033[m")

leiaint("Digite um numero: ")