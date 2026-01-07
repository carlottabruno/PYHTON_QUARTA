# 2. Scacchiera
# Disegnare una scacchiera 8×8 con caselle alternate bianche e nere.
# lato_casella = 40

import turtle

lato_casella = 40

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

for riga in range(8):
    for colonna in range(8):

        if (riga + colonna) % 2 == 0:
            turtle.pencolor("black")
        else:
            turtle.pencolor("grey")

        for i in range(4):
            turtle.forward(lato_casella)
            turtle.right(90)

        turtle.forward(lato_casella)

    turtle.backward(lato_casella * 8)
    turtle.right(90)
    turtle.forward(lato_casella)
    turtle.left(90)

turtle.mainloop()