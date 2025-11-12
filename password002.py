password = input("Inserisci una password: ")
passwordBlanked = password[0] + "*" *  (len(password) - 1) 

print(f"Hai inserito la password: {passwordBlanked}")