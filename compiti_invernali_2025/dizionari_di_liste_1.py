# Registro presenze
# Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti.
# Scrivere funzioni per: 
# (a) contare le presenze di uno studente, 
# (b) trovare chi ha più presenze, 
# (c) trovare chi era presente in una certa data.

def numero_presenze(presenze, studente):
    n = 0
    for alunno in presenze:
        if alunno == studente:
            n = len(presenze[alunno])
    return n

def piu_presenze(presenze):
    massimo = 0

    for alunno in presenze:
        if massimo < len(presenze[alunno]):
            massimo = len(presenze[alunno])
            max = alunno
    
    return max

def trova_data(presenze, data):
    lista = []
    for alunno in presenze:
        if data in presenze[alunno]:
            lista.append(alunno)
    return lista

def main():
    presenze = {
        "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
        "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
        "Luca": ["2024-01-10", "2024-01-11"],
        "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }
    
    nPresenze = numero_presenze(presenze, "Sara")
    print(nPresenze)

    piuPresenze = piu_presenze(presenze)
    print(piuPresenze)

    chi = trova_data(presenze, "2024-01-11")
    print(chi)

if __name__ == "__main__":
    main()