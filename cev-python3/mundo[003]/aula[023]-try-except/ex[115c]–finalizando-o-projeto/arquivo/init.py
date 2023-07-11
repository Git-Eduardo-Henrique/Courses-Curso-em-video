"""
Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
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
        lercriar()
    else:
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"nome: {dado[0]} | idade: {dado[1]}")
    finally:
        a.close()

def cadastro(nome = "", idade=""):
    try:
        a = open("dados.txt", "at") 
    except:
        lercriar()
    else:
        a.write(f"{nome};{idade}\n")
    finally:
        a.close()