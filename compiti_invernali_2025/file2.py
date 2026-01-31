# Conta righe e parole
# Leggere un file di testo e stampare: 
# numero di righe, numero di parole, numero di caratteri (esclusi gli spazi).

def main():
    file = open("testo.txt", "r")
    righe = file.readlines()
    file.close()

    print(f"Il numero di righe è {len(righe)}")

    nParole = 0
    nCaratteri = 0

    for riga in righe:
        parole = riga.split()          
        nParole += len(parole)

        for carattere in riga:
            if carattere != " " and carattere != "\n":
                nCaratteri += 1
    
    print(nParole)
    print(nCaratteri)


if __name__ == "__main__":
    main()