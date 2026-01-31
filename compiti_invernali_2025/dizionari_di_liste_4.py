# Squadre e giocatori
# Un dizionario associa nomi di squadre a liste di giocatori. Scrivere funzioni per: 
# (a) trovare la squadra con più giocatori, 
# (b) verificare se un giocatore è in una squadra, 
# (c) trasferire un giocatore da una squadra all’altra.

def piu_giocatori(squadre):
    nome_max = ""
    max_giocatori = 0

    for squadra in squadre:
        num = len(squadre[squadra])
        if num > max_giocatori:
            max_giocatori = num
            nome_max = squadra

    return nome_max

def trova_giocatore(squadre, giocatore):
    for squadra in squadre:
        if giocatore in squadre[squadra]:
            return True
    return False

def main():
    squadre = {
    "Juventus": ["Vlahovic", "Chiesa", "Locatelli", "Bremer"],
    "Inter": ["Lautaro", "Thuram", "Barella", "Bastoni", "Calhanoglu"],
    "Milan": ["Leao", "Theo", "Reijnders"]
    }

    maggiore = piu_giocatori(squadre)
    print(maggiore)

    giocatore = input("G: ")
    ok = trova_giocatore(squadre, giocatore)

if __name__ == "__main__":
    main()