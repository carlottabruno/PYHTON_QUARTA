# Traduttore di parole
# Dato un dizionario italiano-inglese e una frase in italiano, restituire la frase tradotta. Se
# una parola non è nel dizionario, lasciarla invariata.
# dizionario = {
# "ciao": "hello",
# "mondo": "world",
# "casa": "house",
# "gatto": "cat",
# "cane": "dog",
# "libro": "book",
# "albero": "tree" }
# frase = "ciao mondo il gatto è in casa"

def main():
    dizionario = {
        "ciao": "hello",
        "mondo": "world",
        "casa": "house",
        "gatto": "cat",
        "cane": "dog",
        "libro": "book",
        "albero": "tree"
    }

    frase = "ciao mondo il gatto è in casa"

    parole = frase.split()
    nuova_frase = ""

    for parola in parole:
        if parola in dizionario:
            nuova_frase += dizionario[parola] + " "
        else:
            nuova_frase += parola + " "

    print(f"La frase tradotta è: {nuova_frase}")

if __name__ == "__main__":
    main()

