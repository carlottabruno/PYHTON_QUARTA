# Elementi comuni
# Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.
# lista_a = [1, 5, 8, 12, 15, 20]
# lista_b = [3, 5, 10, 12, 18, 20, 25]

def elementi_comuni(lista_a, lista_b):
    lista_nuova = []
    for a in lista_a:
        if a in lista_b:
            lista_nuova.append(a)

    return lista_nuova

def main():
    lista_a = [1, 5, 8, 12, 15, 20] 
    lista_b = [3, 5, 10, 12, 18, 20, 25]
    lista_nuova = elementi_comuni(lista_a, lista_b)
    
    print(f"La nuova lista è: {lista_nuova}")

if __name__ == "__main__":
    main()