lista = ["Luca", "Mario", "Alice", "Giovanni"]

nmax = 0
nomemax = ""

for nome in lista:
    n = len(nome)
    if n > nmax:
        nmax = n
        nomemax = nome

print(nomemax)