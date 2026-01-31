# Catalogo libri
# Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni per: 
# (a) cercare libri di un autore, 
# (b) calcolare il prezzo medio, 
# (c) trovare il libro più recente.

def cercare_autore(libri, autore):
    libri_autore = []

    for l in libri: # ogni libro è un dizionario
        if l["autore"].lower() == autore.lower():
            libri_autore.append(l)

    return libri_autore

def calcola_prezzo_medio(libri):
    prezzo = 0.0

    for l in libri:
        prezzo += l["prezzo"]
    
    return prezzo / len(libri)

def trova_libro_recente(libri):
    libro_max = libri[0]
    massimo = libro_max["anno"]

    for l in libri:
        if l["anno"] > massimo:
            libro_max = l
    
    return libro_max

def main():
    libri = [
        {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
        {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
        {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
        {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
        {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]

    autore = input("Inserisci l'autore: ")
    libri_autore = cercare_autore(libri, autore)
    print(f"\nI libri con autore {autore} sono: {libri_autore}")

    prezzo_medio = calcola_prezzo_medio(libri)
    print(f"\nIl prezzo medio è {prezzo_medio}")

    libro_recente = trova_libro_recente(libri)
    print(f"\nIl libro più recente è: {libro_recente}")

if __name__ == "__main__":
    main()