print(30 * "\033[33m=-=", "\033[m")
digitado = float(input("digite qualquer numero: "))
print(30 * "\033[33m=-=", "\033[m")

veri_par = digitado % 2 == 0

if veri_par:
    print(f'o numero {digitado} é par')
else:
    print(f'o numero {digitado} é impar')

print(30 * "\033[33m=-=", "\033[m")