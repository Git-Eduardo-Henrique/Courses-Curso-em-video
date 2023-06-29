"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
print(30 * "\033[34m=-=", "\033[m")
print(f"{'10 termos da PA':^90}")
print(30 * "\033[34m=-=", "\033[m")

while True:
    print("digite 0 na razão para fechar...")
    print(30 * "\033[34m=-=", "\033[m")

    termo = int(input("digite o primeiro termo: "))
    razao = int(input("digite a rezão: "))

    if razao == 0:
        break 

    cont = 1

    print(30 * "\033[34m=-=", "\033[m\n")
    while cont <= 10:
        print(f"{termo} ->", end=" ")
        termo += razao
        cont += 1
    
    print("ACABOU! \n")
    print(30 * "\033[34m=-=", "\033[m")
    
print(30 * "\033[34m=-=", "\033[m")
