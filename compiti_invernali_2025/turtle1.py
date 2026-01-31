# Poligono regolare
# Scrivere una funzione che disegni un poligono regolare dato il numero di lati e la lunghezza del lato.
# Esempi di chiamata:
# poligono(4, 100) # quadrato
# poligono(6, 80) # esagono
# poligono(8, 60) # ottagono

import turtle

def sposta(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def poligono(lati, lunghezza):
    angolo = 360 / lati

    for _ in range(lati):
        turtle.forward(lunghezza)
        turtle.left(angolo)

def main():
    nPoligoni = 4
    lato = 100
    shift = 150
    x0, y0 = -250, -lato / 2

    for i in range(nPoligoni):
        y = y0
        x = x0 + shift * i
        sposta(x, y)
        poligono(i + 3, lato)

    turtle.mainloop()

if __name__ == "__main__":
    main()