"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como 
parâmetro e mostre uma mensagem com tamanho adaptável.                                  
Ex:          

escreva('Olá, Mundo!') Saída:                                                                                                                          
 ~~~~~~~~~                                                                                                                                                            
  Olá, Mundo!                                                                                                                                                          
 ~~~~~~~~~     
"""
def escrever(text = ""):
    tam = len(text) + 2
    print(tam * "~")
    print(f"{text:^{tam}}")
    print(tam * "~")

print(30 * "\033[32m=-=", "\033[m")
text = str(input("qual texto vc quer que aparece: "))
print(30 * "\033[32m=-=", "\033[m")

escrever(text="TEXTO ESCRITO ABAIXO!!")
escrever(text=text)

print(30 * "\033[32m=-=", "\033[m")