n = int(input("Quanti numeri di Fibonacci vuoi? "))
a, b = 1, 1 # inizializzazione NON dichiarazione

if n > 2:
    print(a, end=" - ")
    print(b, end=" - ")

    for i in range(n - 2):
        a, b = a + b, a + b + b
        print(a, end=" - ")
        print(b, end=" - ")
        pass # istruzione vuota 
elif n == 2:
    print(a, b)
elif n == 1:
    print(a)
elif n == 0:
    print(f"Nessun numero")

# oppure

a, b = 1, 1 # inizializzazione NON dichiarazione

if n > 2:
    for i in range(n):
        print(a, end=" - ")
        a, b = b, a + b
elif n == 2:
    print(a, b)
elif n == 1:
    print(a)
elif n == 0:
    print(f"Nessun numero")