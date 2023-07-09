"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:
- Quantidade de notas                                                                                                                                                  
- A maior nota                                                                                                                                                                
- A menor nota                                                                                                                                                              
- A média da turma                                                                                                                                                      
- A situação (opcional)
"""
def notas(*n , sit = False):
    dicio = dict()

    dicio["quantidade"] = len(n)
    dicio["maior"] = max(n)
    dicio["menor"] = min(n)
    dicio["media"] = sum(n) / dicio["quantidade"]

    if sit:
        if dicio["media"] >= 7:
            dicio["situacao"] = "Aprovado"
        elif dicio["media"] >= 5:
            dicio["situacao"] = "Recuperação"
        else:
            dicio["situacao"] = "Reprovado"

    return dicio

print(30 * "\033[34m=-=", "\033[m")
print(notas(5.5, 6, 2.3, 9, sit=True))
print(30 * "\033[34m=-=", "\033[m")