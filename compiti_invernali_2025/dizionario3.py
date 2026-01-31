# Voto più frequente
# Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente), 
# trovare quale voto compare più spesso.

def main():
    studenti_voti = {
        "Marco": 7,
        "Sara": 8,
        "Luca": 6,
        "Elena": 8,
        "Paolo": 7,
        "Giulia": 8,
        "Andrea": 6,
        "Chiara": 7
    }

    frequenza = {} 

    for studente in studenti_voti:
        voto = studenti_voti[studente]
        if voto in frequenza:
            frequenza[voto] += 1
        else:
            frequenza[voto] = 1

    max_frequenza = frequenza[6]
    voto_max = 6

    for voto in frequenza:
        if frequenza[voto] > max_frequenza:
            max_frequenza = frequenza[voto]
            voto_max = voto

    print(f"Il voto più frequente è {voto_max} ed è capitato {max_frequenza} volte")

if __name__ == "__main__":
    main()