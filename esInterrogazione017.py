file = open("./valori.csv", "r")
righe = file.readlines()
file.close()

temp = []
umid = []

for riga in righe[1:]:
    fields = riga.split(",")
    temp.append(fields[0])
    umid.append(fields[1])

diz = {}

diz["temp"] = temp
diz["umid"] = umid