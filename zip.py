def main_1():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [ [6, 10, 5],
                   [7, 6],
                   [8, 10, 9, 9],
                   [5, 8] ]

    # voglio stampare il voto a fianco di ogni nome 
    for nome, voto in zip(lista_nomi, lista_voti): # zip mi permette di ciclare contemporaneamente su due liste 
        print(f"{nome}: {voto}")    
    
    # modificare il codice per stampare la media di ognuno, stampare il numero di voti per ognuno, 
    # stampare il voto massimo e il voto minimo

    for nome, voto in zip(lista_nomi, lista_voti): # zip mi permette di ciclare contemporaneamente su due liste 
        max = 0
        media = 0
        
        print(f"{nome}", end=" -> ")
        
        for i in voto:
            media = media + i
        print(f"La media è: {media / i}")

        print(f"I voti sono", end=": ")
        for i in voto:
            print(i, end=" ")
        
        for i in voto:
            if i > max:
                max = i
        
        print(f"\nIl voto massimo è: {max}\n")

if __name__=="__main__": # dunder = double underscore
    main_1()