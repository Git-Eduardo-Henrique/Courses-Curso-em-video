"""
Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
"""
def lercriar():
    try:
        a = open("dados.txt", "rt") 
        a.close()
    except:
        print("arquivo não encontrado | preparando para criar arquivo...")

        try: 
            a = open("dados.txt", "wt+") 
            a.close()

            print("arquivo 'dados.txt' criado com sucesso")
        except:
            print("Erro! ao criar arquivo")

    else:
        print("arquivo carregado com sucesso")

def mostrar():
    try:
        a = open("dados.txt", "rt") 
    except:
        a.close()
        lercriar()
    else:
        print(a.read())
        a.close()