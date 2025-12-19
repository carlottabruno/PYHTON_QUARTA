file = open("./IP.csv", "r")
righe = file.readline()
file.close()

for riga in righe:
    ip = riga.replace(",",".")
    print(ip)
    fields = riga.split(".")

    if fields[-1] == 0:
        print(ip) 