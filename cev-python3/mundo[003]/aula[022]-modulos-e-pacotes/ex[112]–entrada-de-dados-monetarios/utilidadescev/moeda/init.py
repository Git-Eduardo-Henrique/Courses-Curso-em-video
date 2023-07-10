"""
Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação 
de dados para aceitar apenas valores que seja monetários.
"""

def aumentar(num = 0, por = 0, format = False):
    res = num + num * (por / 100)
    if format:
        res = moeda(preco=res)

    return res

def diminuir(num = 0, por = 0, format = False):
    res = num - num * (por / 100 )
    if format:
        res = moeda(preco=res)

    return res

def dobro(num = 0, format = False):
    res = num * 2

    if format:
        res = moeda(preco=res)

    return res

def metade(num = 0, format = False):
    res = num / 2

    if format:
        res = moeda(preco=res)

    return res

def moeda(preco = 0, moeda = "R$"):
    return f"{moeda}{preco:.2f}".replace(".", ",")

# ==================================== 110 ========================================
def resumo(preco = 0, taxa = 0, format = False):
    res = preco
    if format:
        res = moeda(preco=preco)

    print(30 * "\033[36m=-=", "\033[m")
    print(f"o dobro de {res}: {dobro(num=preco, format=format)}\n"
      f"a metade de {res}: {metade(num=preco, format=True)}\n"
      f"aumentando {taxa}%: {aumentar(num=preco, por=taxa, format=True)}\n"
      f"diminuindo {taxa}%: {diminuir(num=preco, por=taxa, format=True)}")
    print(30 * "\033[36m=-=", "\033[m")