# Poligono regolare
# Scrivere una funzione che disegni un poligono regolare dato il numero di lati e la lunghezza del lato.
# Esempi di chiamata:
# poligono(4, 100) # quadrato
# poligono(6, 80) # esagono
# poligono(8, 60) # ottagono

import turtle

def poligono(lati, lunghezza):
    angolo = 360 / lati

    for i in range(lati):
        turtle.forward(lunghezza)
        turtle.right(angolo)

poligono(4, 100)   
turtle.penup()
turtle.forward(150)
turtle.pendown()

poligono(6, 50)    
turtle.penup()
turtle.forward(150)
turtle.pendown()

poligono(8, 30)   

turtle.mainloop()