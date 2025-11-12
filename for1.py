# ci sono tanti modi di fare il for in python
# vediamo il primo modo, detto C-style, tipo quello del c

#range ([START], STOP, [GAP]), start e gap sono parametri facoltativi quindi si scrivono tra quadre 
for i in range(4): # range è una funzione che calcola 4 iterazioni da 0 a 4 escluso 
                   # si può anche scrivere range(0, 4) quindi da 0 a 4 escluso
                   # si può anche mettere il gap range(0, 8, 2) --> 2 è il gap, -2 li salta al contrario
    print(i)

