# 3 crea un programma in python che chiede all'utente una frase/stringa e stampi la stringa 
# inserita un carattere si e uno no (caratteri alternati)

frase = input("Inserisci una frase: ")
frase = frase[::2] # prende ogni carattere in posizione pari, vuol dire salta di 2 (gap)

print(f"La frase è: {frase}")
