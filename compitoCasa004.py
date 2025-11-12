# 4 crea un programma in python che chiede all'utente una frase/stringa e stampi la stringa inserita al contrario

frase = input("Inserisci frase: ")
frase = frase[::-1] # -1 come gap, passi di -1 all'indietro

print(f"Frase al contrario: {frase}")