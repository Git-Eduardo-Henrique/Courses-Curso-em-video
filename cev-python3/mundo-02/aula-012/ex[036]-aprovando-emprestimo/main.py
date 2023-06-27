"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor 
da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou 
então o empréstimo será negado.
"""
print(30 * "\033[33m=-=", "\033[m")
valor = float(input("digite o valor da casa: R$"))
salario = float(input("digite seu salario: R$"))
anos = int(input("digite o total de anos para pagar: "))
print(30 * "\033[33m=-=", "\033[m")

prestacao = valor / (anos * 12)
minimo = salario * 0.3
if prestacao <= minimo:
    print(f"prestações de R${prestacao:.2f}. EMPRESTIMO ACEITO!")
else:
    print(f"prestações de R${prestacao:.2f}. EMPRESTIMO NEGADO!!!")

print(30 * "\033[33m=-=", "\033[m")
