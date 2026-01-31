# Classe quadrato
# Attributi: colore + lato + x e y del vertice in alto a sinistra
# Fuznioni: area, perimetro e disegna (colore pieno).
# Disegna 100 quadrati casuali.

import random
import turtle

class Quadrato():
    def __init__(self, x, y, colore, lato): 
        self.x = x
        self.y = y
        self.colore = colore
        self.lato = lato
    
    def __str__(self):
        return f"(Coordinate ({self.x}; {self.y}), colore: {self.colore}, lato: {self.lato})"

    def area(self):
        return self.lato**2

    def perimetro(self):
        return self.lato * 4

    def disegna(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.colore)
        
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.right(90)
        turtle.end_fill()

def main():
    turtle.speed(0)
    COLORI = ["red", "blue", "green", "purple", "violet", "light blue", "orange", "light green"]

    for _ in range(100):
        colore = random.choice(COLORI)
        x = random.randrange(-300, 300) 
        y = random.randrange(-300, 300) 

        q = Quadrato(x, y, colore, 50)
        q.disegna()

    turtle.mainloop()

if __name__ == "__main__":
    main()