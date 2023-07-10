"""
Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação 
de dados para aceitar apenas valores que seja monetários.
"""
from utilidadescev.moeda.init import *

def lerdinheiro(perg = "", taxa = 0, format = False):
    preco = ""

    while True:
        print(30 * "\033[36m=-=", "\033[m")
        preco = str(input(f"{perg}")).replace(",", ".").strip()

        if not preco.isalpha() and not preco == "":
            resumo(preco=float(preco), taxa=taxa, format=format)
            break
        else:
            print(f'\033[31mErro! "{preco}" não é um valor valido\033[m')
