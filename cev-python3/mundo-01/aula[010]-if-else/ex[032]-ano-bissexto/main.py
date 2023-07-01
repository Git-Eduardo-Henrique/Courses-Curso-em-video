from datetime import date

print(30 * "\033[35m=-=", "\033[m")
ano = int(input("digite o ano (0 para atual): "))
print(30 * "\033[35m=-=", "\033[m")

if ano == 0:
    ano = date.today().year

veri_bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if veri_bissexto:
    print(f"o ano de {ano} é BISSEXTO")
else:
    print(f"o ano de {ano} não é BISSEXTO")    

print(30 * "\033[35m=-=", "\033[m")
