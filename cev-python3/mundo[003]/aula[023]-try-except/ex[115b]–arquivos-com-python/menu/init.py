"""
Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
"""
from arquivo.init import mostrar
from time import sleep

def titulo(txt = "", cor = 37):
    print(f"\033[{cor}m{txt}\033[m".center(90))

def linha(cor = 37):
    print(30 * f"\033[{cor}m=-=", "\033[m")

def iniciarmenu(cor_linha = 37, cor_opt = 37):
    while True:
        opt = 0
        linha(cor=cor_linha)
        titulo(txt="MENU PRINCIPAL", cor=cor_opt)
        linha(cor=cor_linha)

        print(f"\033[{cor_opt}m1 - Pessoas Cadastradas\033[m")
        print(f"\033[{cor_opt}m2 - Cadastrar Pessoa\033[m")
        print(f"\033[{cor_opt}m3 - Sair\033[m")

        while True:
            try:
                linha(cor=cor_linha)
                opt = int(input("Sua opção: "))
            except:
                print("\033[31mvalor invalido!!!\033[m")
            else:
                if opt > 3 or opt < 1:
                    print("\033[31mvalor invalido!!!\033[m")
                else:
                    break
        if opt == 1:
            linha(cor=cor_linha)
            titulo(txt="Pessoas Cadastradas", cor=cor_opt)
            linha(cor=cor_linha)
            mostrar()
            sleep(3)
        elif opt == 2:
            ...
        elif opt == 3:
            linha(cor=cor_linha)
            break
            