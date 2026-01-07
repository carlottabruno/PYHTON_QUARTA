# Voti per materia
# Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: 
# (a) calcolare la media di una materia, 
# (b) trovare la materia con media più alta, 
# (c) aggiungere un voto a una materia.

def media_materia(voti):
    somma = 0

    for v in voti:
        somma += v

    return somma / len(voti)

def media_alta(dizionario):
    media_max = 0

    for materia in dizionario:
        m = media_materia(dizionario[materia])

        if m > media_max:
            media_max = m
            migliore = materia

    return migliore

def aggiungi_voto(dizionario, materia, voto):
    if materia in dizionario:
        dizionario[materia].append(voto)

def main():
    voti_materie = {
        "Matematica": [6, 7, 5, 8, 7],
        "Italiano": [7, 8, 7, 6],
        "Inglese": [8, 8, 9, 7, 8],
        "Informatica": [9, 8, 9, 10, 8]
    }

    print(f"Matematica: {media_materia(voti_materie["Matematica"])}")

    migliore = media_alta(voti_materie)
    print(f"Materia con media più alta: {migliore}")

    aggiungi_voto(voti_materie, "Matematica", 9)
    print(f"Matematica: {voti_materie["Matematica"]}")

if __name__ == "__main__":
    main()
