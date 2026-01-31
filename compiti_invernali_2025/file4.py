# Filtra righe
# Leggere un file e scrivere su un nuovo file solo le righe che contengono una certa parola chiave.

def main():
    file = open("log.txt", "r")
    file2 = open("log2.txt", "w")

    chiave = input("Inserisci una parola chiave: ")

    for riga in file:
        if chiave in riga:
            file2.write(riga)

    file.close()
    file2.close()

if __name__ == "__main__":
    main()