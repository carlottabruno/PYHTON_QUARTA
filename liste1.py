# in python abbiamo le collezioni (insiemi di elementi). Tra le collezioni abbiamo:
# liste, tuple, dizionari, set.

#vediamo le liste

l = [3, 3.14, 10, "ciao", True]

# per accedere agli elementi vigono le stesse regole di INDICIZZAZIONE e SLICING delle stringhe

print(f"L'ultimo elemento della lista è {l[-1]}")
print(l) # stampa tutta la lista
print(f"Tutta la lista senza il primo e l'ultimo elemento {l[1:-1]}")

# aggiunta elemento alla lista
l.append("NUOVO") # NON restituisce nulla, MA MODIFICA!
print(l)

l.pop() # rimuove l'ultimo elemento della lista
print(l)