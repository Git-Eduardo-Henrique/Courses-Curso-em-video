"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um 
dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
print(30 * "\033[31m=-=", "\033[m")
aluno["nome"] = str(input("digite o nome do aluno: "))
aluno["media"] = float(input(f"digite a media do {aluno['nome']}: "))
print(30 * "\033[31m=-=", "\033[m")

if aluno["media"] >= 7:
    aluno["situacao"] = "aprovado"
elif aluno["media"] >= 5 and aluno["media"] < 7:
    aluno["situacao"] = "recuperação"
else:
    aluno["situacao"] = "reprovado"

# .items() mostra a chave e o item
for chave, item in aluno.items():
    print(f"{chave} é igual a {item}")

print(30 * "\033[31m=-=", "\033[m")