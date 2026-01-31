# Squadre e giocatori
# Un dizionario associa nomi di squadre a liste di giocatori. Scrivere funzioni per: 
# (a) trovare la squadra con più giocatori, 
# (b) verificare se un giocatore è in una squadra, 
# (c) trasferire un giocatore da una squadra all’altra.

def piu_giocatori(squadre):
    max = 0
    
    for squadra in squadre:
        if len(squadre[squadra]) > max:
            max = len(squadre[squadra]) 
            sq_max = squadra

    return sq_max

def cerca_giocatore(squadre, giocatore, s):
    for squadra in squadre:
        if s == squadre[squadra]:
            if giocatore in squadre[squadra]:
                return True
    return False

def trasferimento(squadre, giocatore, s2):
    for squadra in squadre:
        if giocatore in squadre[squadra]:
            squadre[s2].append(giocatore)
            squadre[squadra].remove(giocatore)

def main():
    squadre = {
        "Juventus": ["Vlahovic", "Chiesa", "Locatelli", "Bremer"],
        "Inter": ["Lautaro", "Thuram", "Barella", "Bastoni", "Calhanoglu"],
        "Milan": ["Leao", "Theo", "Reijnders"]
    }

    max = piu_giocatori(squadre)
    print(max)

    g = cerca_giocatore(squadre, "Leao", "Juventus")
    print(g)

    trasferimento(squadre, "Leao", "Juventus")
    print(squadre)

if __name__ == "__main__":
    main()