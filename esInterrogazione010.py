mac = input("Inserisci un mac: ")

file = open("./file.csv", "r")
righe = file.readlines()
file.close()

macAdd = []
nome = []

for riga in righe:
    campi = riga.split(",")
    nome.append(campi[0])
    macAdd.append(campi[1])

for n, m in zip(nome, macAdd):
    if mac == m:
        print(n)