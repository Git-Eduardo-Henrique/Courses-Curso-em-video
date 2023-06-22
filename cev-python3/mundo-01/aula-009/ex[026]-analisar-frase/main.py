print(60 * "\033[35m=", "\033[m")
# strip() = remove os espaços da começo e final da frase
frase = str(input("digite uma \033[35mfrase\033[m: ")).upper().strip()
print(60 * "\033[35m=", "\033[m")
# count = conta quantas vezes aparece algo
print(f"\033[35m{frase}\033[m")
print(f"esta frase tem: \033[35m{frase.count('A')}\033[m letras 'A'")
# find = encontra a posição de algo na string a partir da esquerda
print(f"esta frase tem a primeira letra 'A' na posição: \033[35m{frase.find('A')+1}\033[m")
# rfind = encontra a posição de algo na string a partir da direita
print(f"esta frase tem a ultima letra 'A' na posição: \033[35m{frase.rfind('A')+1}\033[m")
print(60 * "\033[35m=", "\033[m")
