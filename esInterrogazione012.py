file = open("./voto.csv", "r")

righe = file.readline()
file.close()

listaNomi = []
listaVoti = []
i = 0
somma = 0

for riga in righe:
    r = riga.split(",")
    listaNomi.append(r[0])
    listaVoti.append(r[1])
    somma += r[1]
    i += 1

media = somma / i
print(f"La media è {media}")
