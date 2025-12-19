def main():
    file = open("./macvendors.csv", "r", encoding="utf-8")
    righe = file.readlines() # righe è una liste di stringhe
    file.close()

    elenco = {}
    elenco2 = {}

    for riga in righe[1:]:  # riga è una stringa
        campi = riga.split(",") # campi è una lista di stringhe 
        elenco[campi[0]] = campi[1]
        elenco2[campi[0]] = campi[-1]

    ricerca = "70:B3:D5:19:B"
  
    if ricerca in elenco:
        print(f"Vendor: {elenco[ricerca]}")
    else:
        print("Vendor non trovato")

    if ricerca in elenco2:
        print(f"Data di produzione: {elenco[ricerca]}")
    else:
        print("Data non trovata")

if __name__ == "__main__":
    main()