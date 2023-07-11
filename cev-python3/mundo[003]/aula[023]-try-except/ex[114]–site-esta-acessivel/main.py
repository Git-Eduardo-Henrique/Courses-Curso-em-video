"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib.request

try:
    urllib.request.urlopen("http://www.pudim.com.br")
except:
    print(30 * "\033[32m=-=", "\033[m")
    print(f"Site indisponivel no momento!!".center(90))
    print(30 * "\033[32m=-=", "\033[m")

else:
    print(30 * "\033[32m=-=", "\033[m")
    print(f"O site do pudim ainda esta no ar!!".center(90))
    print(30 * "\033[32m=-=", "\033[m")