"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

escolhido = randint(0, 10)
tentativas = 0

print(30 * "\033[36m=-=", "\033[m")
print(f'{"Jogo da adivinhação":^90}')
print(30 * "\033[36m=-=", "\033[m")

while True:
    digitado = int(input("Digite um valor entre 0 a 10: "))

    print(30 * "\033[36m=-=", "\033[m")

    print("Processando...")
    sleep(0.5)

    if digitado > 10 or digitado < 0:
        print('Numero invalido')
    elif digitado == escolhido:
        tentativas += 1
        print(f"Acertou!!! o valor é: {escolhido}\nNumero de tentativas: {tentativas}")
        print(30 * "\033[36m=-=", "\033[m")
        break
    else:
        tentativas += 1
        if digitado > escolhido:
            print("Errou!!! tente um valor menor")
        else:
            print("Errou!!! tente um valor maior")

    print(30 * "\033[36m=-=", "\033[m")