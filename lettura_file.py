file = open("./dati.csv", "r") # oggetto file
righe = file.readlines() # fx che restituisce una lista di stringhe contenente le righe del file
file.close()

prima_riga = righe[0]

# unpacking (= spacchettamento)
titolo1, titolo2, titolo3 = prima_riga[:-1].split(",")
print(titolo1)

# leggere tutte le altre righe del file e stamoarle, usare un ciclo for pythonico (senza range)

