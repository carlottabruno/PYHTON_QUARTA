def crea_classifica(d):
    """
    Restituisce una lista di tuple (studente, media) ordinata per media decrescente
    """
    classifica = []

    for i in d:
        classifica.append(i)
        media = calcola_media(i)
        classifica.append(media)

    return classifica

def calcola_media(lista_voti):
    """
    Restituisce la media dei voti
    """
    somma = 0
    count = 0

    for i in lista_voti:
        somma += i
        count += 1

    return somma / count

def leggi_file(nome_file):
    """Legge il file e restituisce un dizionario {studente: [voti]}"""
    file = open(nome_file, "r")
    righe = file.readlines()
    file.close()

    d = {}
    
    for riga in righe:
        lista_voti = []
        fields = riga.split(";")

        for i in fields[1:]:
            lista_voti.append(i)

        d[fields[0]] = lista_voti
    
    return d

def main():
    d = leggi_file("registro2.txt")

    classifica = crea_classifica(d)
    print(classifica)

if __name__ == "__main__":
    main()