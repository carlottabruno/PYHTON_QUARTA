# Parola più frequente
# Leggere un file di testo e trovare la parola che compare più volte (ignorando maiuscole/minuscole).

def main():
    file = open("articolo.txt", "r")
    righe = file.readlines()
    file.close()

    diz = {}

    for riga in righe:
        parole = riga.split()
        for parola in parole:
            if parola in diz:
                diz[parola] += 1
            else:
                diz[parola] = 1
    
    print(diz)

if __name__ == "__main__":
    main()