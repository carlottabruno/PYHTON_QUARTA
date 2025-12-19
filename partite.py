# Simulare n partite a pari e dispari.
# Input utente:
# - n numero di partite
# - nome primo giocatore (quello che vince se esce pari)
# - nome secondo giocatore.

# 1) Per simulare le partite usiamo un dizionario:
# esempio nel caso n = 3
# d = {"Nome giocatore 1" : [3,2,5], "Nome giocatore 2" : [1,2,4]}

# Le singole giocate sono generate con random.randint()

# 2) Creare una lista che contiene i nomi dei vincitori per ogni partita e stamparla.

# Ipotesi: il primo giocatore vince se esce pari, il secondo se esce dispari.

import random

MINIMO = 0
MASSIMO = 5

def simulaPartita(partite):
    lanci = []
    
    for i in range(partite):
        lanci.append(random.randint(MINIMO, MASSIMO))
        lanci.append(random.randint(MINIMO, MASSIMO))
        
    return lanci

def main():
    n = int(input("Quante partite vuoi simulare? "))
    g1 = input("Nome del primo giocatore (vince se esce PARI): ")
    g2 = input("Nome del secondo giocatore (vince se esce DISPARI): ")

    d = {g1 : simulaPartita(n), g2 : simulaPartita(n)}

    print("\nDizionario delle giocate:")
    print(d)

    vincitori = []

    for l1, l2 in zip(d[g1], d[g2]):
        if(l1 + l2) % 2 == 0:
            vincitori.append(g1)
        else:
            vincitori.append(g2)

    print("\nVincitori:\n")
    print(vincitori)

if __name__ == "__main__":
    main()