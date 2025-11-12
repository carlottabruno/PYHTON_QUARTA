# utente inserisce in input una password
# il programma stampa la password oscurata da *

password = input("Inserisci una password: ")
passwordBlanked = "*" *  len(password) # restituisce la lunghezza della stringa di qualsiasi tipo di variabile
print(f"Hai inserito la password: {passwordBlanked}")