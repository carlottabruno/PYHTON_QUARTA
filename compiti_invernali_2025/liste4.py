# Elementi comuni
# Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.
# lista_a = [1, 5, 8, 12, 15, 20]
# lista_b = [3, 5, 10, 12, 18, 20, 25]

def main():
    lista_a = [1, 5, 8, 12, 15, 20]
    lista_b = [3, 5, 10, 12, 18, 20, 25]
    lista_nuova = []

    for a in lista_a:
        if a in lista_b:
            lista_nuova.append(a)

    print(f"La nuova lista è: {lista_nuova}")

if __name__ == "__main__":
    main()