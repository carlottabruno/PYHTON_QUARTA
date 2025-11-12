n = int(input("Inserisci un numero positivo: "))

if n >= 0:
    for i in range(n + 1):
        print(i**2, end=" - ") # per stampare il quadrato
else: 
    print(f"Non si può calcolare")