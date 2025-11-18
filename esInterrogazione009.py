import readline

f = open("./file.csv", "r")

f.readline()

somma = 0
i = 0

for righe in f:
    riga = righe.split(",")
    somma += int(riga[1])
    i += 1

media = float(somma / i)
print(media)

f.close()
    