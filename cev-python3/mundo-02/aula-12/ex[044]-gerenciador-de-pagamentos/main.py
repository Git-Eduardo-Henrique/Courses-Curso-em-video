"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal 
e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros
"""
titulo = "loja do seu zé"
print(30 * "\033[34m=-=", "\033[m")
print(f"{titulo:^90}")
print(30 * "\033[34m=-=", "\033[m")

valor = float(input("valor das suas compras: R$"))

print(30 * "\033[34m=-=", "\033[m")
print("[ 1 ] = à vista ( 10% de desconto )\n[ 2 ] = à vista com cartão ( 5% de desconto )\n[ 3 ] = 2x no cartão\n"
      "[ 4 ] = 3x no cartão ou mais ( 20% de juros )")
print(30 * "\033[34m=-=", "\033[m")

opc = int(input("sua opção: "))
print(30 * "\033[34m=-=", "\033[m")

if opc == 1:
    desco = valor - valor * 0.1
    print(f"sua compra com desconto de 10% deu o valor de: R${desco:.2f}")
elif opc == 2:
    desco = valor - valor * 0.05
    print(f"sua compra com desconto de 5% deu o valor de: R${desco:.2f}")
elif opc == 3:
    parcelas = valor / 2
    print(f"suas parcelas ficaram em: 2x R${parcelas:.2f} | e no total ficou: R${valor:.2f}")
elif opc == 4:
    n_parcelas = int(input("numero de parcelas: "))
    print(30 * "\033[34m=-=", "\033[m")
    if n_parcelas < 3:
        print("as parcelas devem ser maior do que 3 vezes")
    else:
        juros = valor + valor * 0.2
        parcelas = juros / n_parcelas 
        print(f"suas parcelas ficaram em: {n_parcelas}x R${parcelas:.2f} | e no total ficou: R${juros:.2f}")
else:
    print("numero invalido!!")

print(30 * "\033[34m=-=", "\033[m")