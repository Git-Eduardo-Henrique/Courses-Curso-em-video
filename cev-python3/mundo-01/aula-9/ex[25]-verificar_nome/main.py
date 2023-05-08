print(60 * "\033[34m=", "\033[m")
nome = str(input("qual o seu \033[34mnome\033[m: ")).strip()
print(60 * "\033[34m=", "\033[m")

if "SILVA" in nome.upper():
    print("seu nome tem \033[34mSilva\033[m")
else:
    print("seu nome não tem \033[34mSilva\033[m")

print(60 * "\033[34m=", "\033[m")