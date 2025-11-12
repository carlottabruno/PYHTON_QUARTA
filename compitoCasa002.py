# 2 crea un programma in python che chiede all'utente un numero intero e stampa se un numero è divisibile per due, tre o cinque
# Hint: operatore % per il resto della divisione 

num = int(input("Inserisci un umero intero: "))

if num % 2 == 0:
    print(f"Il numero è divisibile per due")
elif num % 3 == 0:
    print(f"Il nuemro è divisibile per tre")
elif num % 5 == 0:
    print(f"Il nuemro è divisibile per cinque")
else:
    print(f"Il numero non è divisibile per due, tre e cinque")