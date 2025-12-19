# numero intero maggiore di 2 all'utente e disegnare un poligono 

import turtle

def main():
    n = int(input("Inserisci quanti lati deve avere il poligono: "))

    if n <= 2:
        print("Il numero di lati deve essere maggiore di 2.")
    else:
        angolo = 360 / n

        for i in range(n):
            turtle.forward(100)
            turtle.left(angolo)

        turtle.mainloop()
    

if __name__ == "__main__":
    main()