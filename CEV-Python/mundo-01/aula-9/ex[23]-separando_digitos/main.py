# =======================================================================
print(60 * "\033[32m=", "\033[m")
num = int(input("digite um \033[32mnumero\033[m entre \033[32m0\033[m e \033[32m9999\033[m: "))
print(60 * "\033[32m=", "\033[m")

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f"{num} - unidade: {uni}")
print(f"{num} - dezena: {dez}")
print(f"{num} - centena: {cen}")
print(f"{num} - milhar: {mil}")
print(60 * "\033[32m=", "\033[m")
