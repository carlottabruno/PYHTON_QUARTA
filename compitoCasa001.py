# 1 crea un programma in python che chiede all'utente il suo nome e lo stampa sempre con l'iniziale maiuscola

nome = input("Inserisci nome -> ")
nome = nome.lower()
nome = nome[0].upper() + nome[1:]

print(f"Il nome maiuscolo è: {nome}")