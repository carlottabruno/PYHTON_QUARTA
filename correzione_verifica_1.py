# Correzione della verifica del 14 gennaio

def temp_media(dati):
    nCitta = 0
    somma_temperature = 0

    for dato in dati:
        somma_temperature += dato["temp"]
        nCitta += 1

    return somma_temperature / nCitta

def filtra_citta(dati, nome):
    lista_temperature_citta = []

    for dato in dati:
        if dato["citta"] == nome:
            lista_temperature_citta.append(dato["temp"])
    
    return lista_temperature_citta

def temp_per_citta(dati): 
    dizionario = {}

    for dato in dati:
        dizionario[dato["citta"]] = filtra_citta(dati, dato["citta"])
    
    return dizionario

def carica_regioni(nome_file):
    dizionario_regioni = {}

    file = open(nome_file, "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        campi = riga.split(";")
        dizionario_regioni[campi[0]] = campi[1][:-1]

    return dizionario_regioni

def main():
    dati = [
        {"citta": "Milano", "temp": 12},
        {"citta": "Roma", "temp": 18},
        {"citta": "Milano", "temp": 14},
        {"citta": "Napoli", "temp": 20},
        {"citta": "Roma", "temp": 17},
        {"citta": "Napoli", "temp": 22},
        {"citta": "Milano", "temp": 10}
    ]

    media = temp_media(dati)
    print(f"\nMedia delle temperature: {media: .2f}.")

    citta = "Milano"
    temperature_citta = filtra_citta(dati, citta)
    print(f"\nTemperature della città di {citta}: {temperature_citta}.")

    dizionario_per_citta = temp_per_citta(dati)
    print(f"\nDizionario con le temperature delle citta: {dizionario_per_citta}.")

    dizionario_regioni = carica_regioni("regioni.txt")
    print(f"\nDizionario delle regioni: {dizionario_regioni}.\n")

if __name__ == "__main__":
    main()