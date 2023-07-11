"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da 
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiafloat(perg = ""):
    while True:
        print(30 * "\033[31m=-=", "\033[m")
        try:
            num = float(input(f"{perg}"))
            break
        except:
            print("\033[31mDIGITE UM NUMERO DECIMAL!!!\033[m")

    print(30 * "\033[31m=-=", "\033[m")
    print(f"{f'você digitou o numero {num}':^90}")

def leiaint(perg = ""):
    while True:
        print(30 * "\033[31m=-=", "\033[m")
        try:
            num = int(input(f"{perg}"))
            break
        except:
            print("\033[31mDIGITE UM NUMERO INTEIRO!!!\033[m")

    print(30 * "\033[31m=-=", "\033[m")
    print(f"{f'você digitou o numero {num}':^90}")

leiaint("Digite um numero inteiro: ")
leiafloat("Digite um numero decimal: ")

print(30 * "\033[31m=-=", "\033[m")