"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
produtos = ("todinho", 4.5, "farofa pronta yoki", 6.49, "danoninho", 7, "margarina", 6, "air fryer", 324.99)

print(30 * "\033[35m=-=", "\033[m")
print(f"{'lojas 500':^90}")
print(30 * "\033[35m=-=", "\033[m")

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f"{produtos[item]:.<30} | ", end="")
    else:
        print(f"R${produtos[item]:.2f}")

print(30 * "\033[35m=-=", "\033[m")