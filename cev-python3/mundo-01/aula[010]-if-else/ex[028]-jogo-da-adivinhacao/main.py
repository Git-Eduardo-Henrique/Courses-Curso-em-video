from random import randint
from time import sleep

escolhido = randint(0, 5)

print(30 * "\033[31m=-=", "\033[m")
print(f'{"Jogo da adivinhação":^90}')
print(30 * "\033[31m=-=", "\033[m")

digitado = int(input("Digite um valor entre 0 a 5: "))

print(30 * "\033[31m=-=", "\033[m")

print("Processando...")
sleep(1.5)

print(30 * "\033[31m=-=", "\033[m")
if digitado > 5:
    print('Numero invalido')
elif digitado == escolhido:
    print(f"Acertou!!! o valor é: {escolhido}")
else:
    print(f"Errou!!! voce digitou {digitado} e o valor é: {escolhido}")

print(30 * "\033[31m=-=", "\033[m")
