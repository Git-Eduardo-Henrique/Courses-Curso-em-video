"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de 
Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
times = ("Botafogo", "Grêmio", "Flamengo", "Red Bull Bragantino", "Palmeiras", "Fluminense", "São Paulo", "Internacional",
         "Fortaleza", "Athletico-PR", "Atlético-MG", "Cruzeiro", "Santos", "Bahia", "Corinthians", "Cuiabá", "Goiás",
         "Vasco", "América-MG", "Coritiba")

print(30 * "\033[32m=-=", "\033[m")
print(f"cinco primeiros times: {times[0:5]}")
print(f"ultimos quatro colocados: {times[-4:]}")
print(f"posição do palmeiras: {times.index('Palmeiras')+1}")
print(30 * "\033[32m=-=", "\033[m")
print(f"ordem alfabetica: {sorted(times)}")
print(30 * "\033[32m=-=", "\033[m")