# Playlist
# Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
# (a) contare le canzoni totali, 
# (b) cercare in quale playlist si trova una canzone, 
# (c) unire due playlist in una nuova.

def canzoni_totali(playlist):
    totale = 0
    
    for genere in playlist:
        totale += len(playlist[genere])
    
    return totale

def trova_canzone(playlist, canzone):
    trovati = []

    for generi in playlist:
        for lista in playlist[generi]:
            if canzone in lista:
                trovati.append(generi)
    
    return trovati

def merge_playlist(playlist, p1, p2):
    lista = []
    lista.append(p1)

    for p in playlist: 
        if p == p2:
            lista.append(p2[p])
    
    return lista

def main():
    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }

    canzoni_tot = canzoni_totali(playlist)
    print(f"\nLe canzoni totali sono {canzoni_tot}")

    canzone = input("Inserisci una canzone: ")
    playlists = trova_canzone(playlist, canzone)
    print(f"La canzone {canzone} si trova in: {playlists}")

    p1 = input("Inserisci la prima playlist: ") # gli passo i generi
    p2 = input("Inserisci la seconda playlist: ")
    lista = merge_playlist(playlist, p1, p2)
    print(f"unire le playlist: {lista}")

if __name__ == "__main__":
    main()