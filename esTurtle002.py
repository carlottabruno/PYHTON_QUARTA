# Il file disegno.txt contiene istruzioni per realizzare un disegno, una per riga.
# Dopo aver consultato: https://docs.python.org/3/library/turtle.html scrivi un programma che:
# legga il file di comandi;
# interpreti ed esegua ogni comando usando turtle.

# avanti 100
# destra 90
# avanti 100
# destra 90
# colore rosso
# avanti 100
# destra 90
# avanti 100
# salta 150 0
# cerchio 50

#turtle.pencolor("red")

import turtle

def main():
    file = open("./disegno.txt", "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        comandi = riga.split(" ")

        if comandi[0] == "avanti":
            turtle.forward(int(comandi[1]))
        
        if comandi[0] == "destra":
            turtle.right(int(comandi[1]))

        if comandi[0] == "sinistra":
            turtle.left(int(comandi[1]))
        
        if comandi[0] == "colore":
            if comandi[1] == "rosso":
                comandi[1] = "red"
                turtle.pencolor(comandi[1])
        
        if comandi[0] == "salta":
            turtle.penup()
            turtle.goto(int(comandi[1]), int(comandi[2]))
            turtle.pendown()
        
        if comandi[0] == "cerchio":
            turtle.circle(int(comandi[1]))
        
        turtle.mainloop()

if __name__ == "__main__":
    main()