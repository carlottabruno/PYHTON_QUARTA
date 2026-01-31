# secondo massimo

def secondo_massimo(valori):
    massimo = valori[0]
    minimo = valori[0]

    # cerco massimo e minimo
    for v in valori:
        if v > massimo:
            massimo = v
        if v < minimo:
            minimo = v
    
    # assegno a secondo massimo il valore più piccolo dell'array
    secondoMassimo = minimo

    # cerco valore più grande che sia diverso dal massimo
    for v in valori: 
        if (v > secondo_massimo) and (v != massimo):
            secondo_massimo = v
    
    return secondoMassimo

def main():
    valori = [45, 12, 23, 68, 56]
    secondoMassimo = secondo_massimo(valori)
    print(secondoMassimo)