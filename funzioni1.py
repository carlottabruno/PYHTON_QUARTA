# MODULARITA': suddividere il codice in funzioni.
# documenta la funzione """""" oppure '''''' (= docstring) 
# print(help(primaLetteraMaiuscola)) restituisce la docstring

# COSTANTE è una variabile globale 
# ATTENZIONE: COSTANTE è accessibile da tutte le funzioni solo in LETTTURA

COSTANTE = 3.14

def primaLetteraMaiuscola(stringa):
    """ 
    DOCSTRING: La funzione restituisce stringa con la lettera iniziale maiuscola.
    """
    # stringa è una VARIABILE LOCALE alla funzione
    s = stringa[0].upper() + stringa[1:].lower()
    return s

def media(lista):
    """
    La funzione restituisce la media dei valori presenti in lista
    e il numero di elementi di lista.
    """
    somma = 0. # . perche mi aspetto una lista di float
    n_lista = len(lista)

    for val in lista: # val è il VALORE NON l'indice
        somma += val

    return somma/n_lista, n_lista

def main():
    # print(help(primaLetteraMaiuscola))
    nome = input("Inserisci una parola: ")
    print(primaLetteraMaiuscola(nome))

    voti = [4.5, 10, 8.25, 7, 6]
    m, n = media(voti)
    print(f"La media è {m} e il numero di voti è {n}.")

if __name__=="__main__":
    main()