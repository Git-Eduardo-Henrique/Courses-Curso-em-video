"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem 
no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""
print(30 * "\033[31m=-=", "\033[m")
nota1 = float(input("primeira nota: "))
nota2 = float(input("segundo nota: "))
print(30 * "\033[31m=-=", "\033[m")

media = (nota1 + nota2) / 2

print(f"sua media foi de {media}")
if media < 5:
    print("você foi REPROVADO!")
elif 7 > media >= 5:
    print("você está de RECUPERAÇÃO!!")
else:
    print("você foi APROVADO!")

print(30 * "\033[31m=-=", "\033[m")