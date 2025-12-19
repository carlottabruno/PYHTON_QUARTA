ALFABETO = "abcdefghijklmnopqrstuvwxyz"

def stampa_frequenze(dizionario, percentuali, alfabeto):
    """
    La funzione stampa le frequenze delle lettere fornite.
    Inout:
        - dizionario : contiene le frequenze assolute per tutte le lettere
        - alfabeto: stringa contenente le lettere di interesse
    Output:
        - None
    """

    print("=" * 30)

    for lettera in alfabeto:
        if lettera in dizionario:
            print(f"{lettera} - {dizionario[lettera]} - {percentuali[lettera]: .2f} %")
        else: 
            print(f"{lettera} - 0 - 0.00 %")
    
    print("=" * 30)

def calcola_percentuale(dizionario, totale_lettere):
    return {car: (dizionario[car] * 100) / totale_lettere for car in dizionario}

def main():
    print(f"Apretura file...")
    file = open("./testo.txt", "r", encoding = "utf-8")
    testo = file.read()
    file.close()
    print(f"Letti {len(testo)} caratteri.")
    print()

    dizionario = {}
    totale_lettere = 0

    print("=" * 30)
    for car in testo:
        if car.isalpha():
            car = car.lower()
            totale_lettere += 1

            if car in ALFABETO:
                if car in dizionario:
                    dizionario[car] += 1
                else:
                    dizionario[car] = 1

    
    percentuali = calcola_percentuale(dizionario, totale_lettere)

    stampa_frequenze(dizionario, percentuali, ALFABETO)

if __name__ == "__main__":
    main()