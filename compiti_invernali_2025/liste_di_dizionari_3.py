# Filtro prodotti
# Una lista contiene dizionari con chiavi nome, categoria, prezzo. Scrivere una funzione
# che restituisca solo i prodotti di una certa categoria con prezzo inferiore a un valore dato.

def prodotti_categoria(cat, prezzo_limite, prodotti):
    risultato = []

    for p in prodotti:
        if p["categoria"] == cat:
            if p["prezzo"] < prezzo_limite:
                risultato.append(p)

    return risultato

def main():
    prodotti = [
        {"nome": "Laptop", "categoria": "elettronica", "prezzo": 899.99},
        {"nome": "Mouse", "categoria": "elettronica", "prezzo": 29.99},
        {"nome": "Scrivania", "categoria": "arredamento", "prezzo": 199.99},
        {"nome": "Tastiera", "categoria": "elettronica", "prezzo": 79.99},
        {"nome": "Sedia", "categoria": "arredamento", "prezzo": 149.99},
        {"nome": "Monitor", "categoria": "elettronica", "prezzo": 349.99}
    ]

    filtrati = prodotti_categoria("elettronica", 100, prodotti)

    for p in filtrati:
        print(p)

if __name__ == "__main__":
    main()
