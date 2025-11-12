# in python possiamo delimitare con "" oppure con ''
stringa = "Ciao mondo!"
print(stringa)

# esempio di indicizzazione della stringa (indicizzare = estrarre un elemento)
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

# esempio di slicing delle stringhe 
print(f"La sottostringa 2-5 è {stringa[2:5]}.") # da posizione 2 incluso a 5 escluso (indice a sinistra incluso, quello a destra escluso)

nome, cognome = "Mario", "Rossi" # ASSEGNAZIONE MULTIPLA (vale per ogni tipo di dato)
spazio = " "
x = nome + spazio + cognome # CONCATENAZIONE STRINGHE
print(x)

x = nome + " " + cognome # oppure
print(x)

#CONCATENAZIONE MULTIPLA di una stringa con se stessa
y = nome * 5
print(y)