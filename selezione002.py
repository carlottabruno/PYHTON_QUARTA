print("premi A per inserire.")
print("premi B per modificare.")
print("premi C per cancellare.")

tasto = input("-> ")
tasto = tasto.upper() # trasforma tutto in maiuscolo!
                      # .lower() trasforma tutto in maiuscolo
                      # upper e lower sono dei METODI non funzioni

if tasto == "A":
    print("L'utente vuole inserire")
elif tasto == "B":
    print("L'utente vuole modificare")
elif tasto == "B":
    print("L'utente vuole calcellare")
else:
    print("Tasto non valido")
