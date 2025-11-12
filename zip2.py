# modificare il codice per stampare la media di ognuno, 
# stampare il numero di voti per ognuno, 
# stampare il voto massimo e il voto minimo

def main_1():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [ [6, 10, 5],
                   [7, 6],
                   [8, 10, 9, 9],
                   [5, 8] ] 
    
    for nome, voti in zip(lista_nomi, lista_voti): 
        print(f"{nome}: ")

        somma = 0
        voto_max = voti[0]
        voto_min = voti[0]

        for voto in voti:
            somma = somma + voto

            if voto > voto_max:
                voto_max = voto
            if voto < voto_min:
                voto_min = voto

            media = somma / len(voti)

        print(f"Voti:", end=" ")
        for voto in voti:
            print(f"{voto}", end=" ")

        print(f"\nMedia: {media}")
        print(f"Numero di voti: {len(voti)}")
        print(f"Voto massimo: {voto_max}")
        print(f"Voto minimo: {voto_min}\n")

if __name__=="__main__": 
    main_1()