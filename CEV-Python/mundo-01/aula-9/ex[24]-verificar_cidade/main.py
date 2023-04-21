print(60 * "\033[33m=", "\033[m")
cidade = str(input("qual o nome da sua \033[33mcidade\033[m: ")).strip()
print(60 * "\033[33m=", "\033[m")

if cidade[:5].upper() == "SANTO":
    print("sua cidade começa com \033[33mSanto\033[m")
else:
    print("sua cidade não começa com \033[33mSanto\033[m")

print(60 * "\033[33m=", "\033[m")