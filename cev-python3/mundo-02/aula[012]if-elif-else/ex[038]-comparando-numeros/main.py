"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior   
Não existe valor maior, os dois são iguais
"""
print(30 * "\033[35m=-=", "\033[m")
num1 = int(input("digite o primeiro numero inteiro: ")) 
num2 = int(input("digite o segundo numero inteiro: ")) 
print(30 * "\033[35m=-=", "\033[m")

if num1 > num2:
    print(f"o numero {num1} é maior que {num2}")
elif num2 > num1:
    print(f"o numero {num2} é maior que {num1}")
else:
    print(f"o numeros {num1} e {num2} são iguais")

print(30 * "\033[35m=-=", "\033[m")