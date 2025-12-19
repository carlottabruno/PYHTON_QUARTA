# Il file registro.txt contiene i voti degli studenti di una classe, con questo formato:

# Bianchi Mario;7;8;6;9;7
# Esposito Lucia;8;9;8;8 
# Ferraro Ahmed;6;5;7;6;8;7 
# Greco Sofia;9;8;9

# Ogni riga contiene cognome e nome, seguiti dai voti separati da punto e virgola. 
# Gli studenti possono avere un numero diverso di voti.

# Scrivi un programma che:
# Legga il file e costruisca un dizionario {nome: [lista_voti]}
# Calcoli la media di ogni studente
# Produca una classifica ordinata per media decrescente
# Mostri il "podio" (i primi 3) 
# e gli studenti in difficoltà (media < 6)

# Implementa e usa le funzioni presenti in traccia.py

def leggi_registro(nome_file):
    """Restituisce un dizionario {nome: [voti]}."""
    file = open(nome_file, "r")
    testo = file.readlines()
    file.close()

    dizionario = {}

    for riga in testo:
        fields = riga.split(";")
        nome = fields[0]

        voti = []

        for v in fields[1:]:
            voti.append(v)
        
        dizionario[nome] = voti

    return dizionario

def calcola_media(voti):
    """Restituisce la media di una lista di voti."""
    media = 0
    count = 0
    
    for voto in voti:
        media += int(voto)
        count += 1
    
    media /= count
    
    return media

def classifica(registro):
    """
    Restituisce una lista di tuple (nome, media) 
    ordinata per media decrescente.
    """
    lista = []
    for nome in registro:
        lista.append((nome, registro[nome]))

    n = len(lista)

    for i in range(n):
        for j in range(n - i - 1):
            if lista[j][1] < lista[j + 1][1]:   
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def stampa_podio(classifica):
    """Stampa i primi 3 della classifica (usa slicing)."""
    for nome, media in classifica[:3]:
        print(f"{nome}: {media}")

def trova_insufficienti(classifica):
    """Restituisce la lista degli studenti con media < 6."""
    
    for nome, media in classifica:
        if media < 6:
            print(f"{nome}: {media}")

def main():
    dizionario = leggi_registro("./registro.txt")
    registro = {}

    for nome in dizionario:
        voti = dizionario[nome]
        media = calcola_media(voti)
        registro[nome] = media
    
    classifica_finale = classifica(registro)

    print("\nPODIO: ")
    stampa_podio(classifica_finale)

    print("\nStudenti insufficienti: ")
    trova_insufficienti(classifica_finale)

if __name__ == "__main__":
    main()