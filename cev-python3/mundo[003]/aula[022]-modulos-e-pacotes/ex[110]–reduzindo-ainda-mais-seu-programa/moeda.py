"""
Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
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

    print(f"o dobro de {res}: {dobro(num=preco, format=format)}\n"
      f"a metade de {res}: {metade(num=preco, format=True)}\n"
      f"aumentando {taxa}%: {aumentar(num=preco, por=taxa, format=True)}\n"
      f"diminuindo {taxa}%: {diminuir(num=preco, por=taxa, format=True)}")