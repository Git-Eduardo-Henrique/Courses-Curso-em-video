print(60 * "\033[36m=", "\033[m")
# strip() = remove os espaços da começo e final da frase
nome = str(input("digite seu \033[36mnome completo\033[m: ")).upper().strip()
nome_split = nome.split() # split = separa cada palavra de uma string
print(60 * "\033[36m=", "\033[m")
# count = conta quantas vezes aparece algo
print(f"\033[36m{nome}\033[m")
print(f"seu primeiro nome: \033[36m{nome_split[0]}\033[m")
print(f"seu ultimo nome: \033[36m{nome_split[len(nome_split)-1]}\033[m")

print(60 * "\033[36m=", "\033[m")