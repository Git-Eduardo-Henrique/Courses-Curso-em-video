"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
pilha = []

print(30 * "\033[36m=-=", "\033[m")
expre = str(input("digite uma expressão: "))
print(30 * "\033[36m=-=", "\033[m")

for letra in expre:
    if letra == "(":
        pilha.append(letra)
    elif letra == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(letra)
            break

if len(pilha) == 0:
    print("esta expressão esta correta")
else:
    print("esta expressão esta completamente errada")

print(30 * "\033[36m=-=", "\033[m")