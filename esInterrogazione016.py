comandi = {0 : "forward", 1 : "backward", 2 : "left", 3 : "right"}

file = open("./interrog.csv", "r")
righe = file.readlines()
file.close()

for riga in righe:
    riga = int(riga)
    print(comandi[riga])