# 4 operazioni aritmetiche, chiedere quale operazione si vuole eseguire
# chiede due numeri e stampa il risultato

print(f"0 - Somma")
print(f"1 - Sottrazione")
print(f"2 - Moltiplicazione")
print(f"3 - Divisione")
risposta = int(input("Quale operazione vuoi effettuare? "))

a = int(input("Inserisci un numero: "))
b = int(input("Inserisci un numero: "))

if risposta == 0:
    ris = a + b
elif risposta == 1:
    ris = a - b
elif risposta == 2:
    ris = a * b
elif risposta == 3:
    ris = a // b

print(ris)
