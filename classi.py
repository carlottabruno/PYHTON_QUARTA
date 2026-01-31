# In Pyhon tutto è un oggetto! Anche int o float sono oggetti
# Anche le funzioni sono oggetti.

# Creare classi ci permette di creare nuovi oggetti!

import math
import turtle

class Punto():
    # costruttore viene chiamato da Punto()
    def __init__(self, x, y): # self è come list in Java 
        # attributi (in Python tutto è PUBBLICO)
        self.x = x
        self.y = y
    
    def __str__(self):
    # deve rimanere una stringa
        return f"({self.x}, {self.y})"
    
    def distanza_origine(self):
        # ritorna la distanza del punto dall'origine 0, 0
        return math.sqrt(self.x**2 + self.y**2)
    
    def scambia_coordinate(self):
        # questo metodo ritorna un nuovo punto con x e y scambiate
        return Punto(self.y, self.x)

    def disegna(self):
        # questo metodo usa turtle per disegnare il punto
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.dot(10)
        turtle.mainloop()
    
    def distanza(self, altro):
        # restituisce la distanza tra due punti
        # altro è un'istanza di un altro punto
        return math.sqrt((self.x - altro.x)**2 + (self.y - altro.y)**2)

def main():
    a = Punto(1, 2) # ho creato un'istanza
    print(a)
    print(f"Il punto dista {a.distanza_origine()}")

    b = a.scambia_coordinate()
    print(b)

    a.disegna()

    distanza = a.distanza(b)
    print(f"La distanza tra i due punti è {distanza: .2f}")

if __name__ == "__main__":
    main()