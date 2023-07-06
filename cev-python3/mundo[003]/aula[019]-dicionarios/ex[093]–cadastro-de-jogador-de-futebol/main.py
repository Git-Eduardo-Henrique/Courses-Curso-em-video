"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler 
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
dados = dict()
gols = list()
totalgols = 0

print(30 * "\033[34m=-=", "\033[m")
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas jogadas'] = int(input(f'digite as quantas partidas {dados["nome"]} jogou: '))

for cont in range(0, dados['partidas jogadas']):
    gols.append(int(input(f'digite os gols da {cont+1}° partida: ')))
    totalgols += gols[cont]

dados['gols'] = gols.copy()
dados['total'] = totalgols

print(30 * "\033[34m=-=", "\033[m")

for chave, item in dados.items():
    print(f'{chave}: {item}')

print(30 * "\033[34m=-=", "\033[m")

print(f'O jogador {dados["nome"]} jogou {dados["partidas jogadas"]} jogos.')

for chave, items in enumerate(dados["gols"]):
    print(f'Na {chave+1}° partida fez {items} gols.')

print(f'Foi um total de {dados["total"]} gols.')
print(30 * "\033[34m=-=", "\033[m")