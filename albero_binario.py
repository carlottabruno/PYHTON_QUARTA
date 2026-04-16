class Nodo:
    """Nodo autoreferenziale per albero binario."""

    def __init__(self, valore, sx=None, dx=None):
        self.valore = valore
        self.sx = sx
        self.dx = dx

    def inserisci(self, valore):
        if valore < self.valore:
            if self.sx == None:
                self.sx = Nodo(valore)
            else:
                self.sx.inserisci(valore)
        else:
            if self.dx == None:
                self.dx = Nodo(valore)
            else:
                self.dx.inserisci(valore)
            
    def cerca(self, valore):
        if valore == self.valore:
            return True
        
        if valore < self.valore:
            if self.sx == None:
                return False
            return self.sx.cerca(valore)
        else:
            if self.dx == None:
                return False
            return self.dx.cerca(valore)            

# Esempio d'uso
radice = Nodo(5)
for v in [3, 7, 1, 4, 6, 8]:
    radice.inserisci(v)
print(radice)

print(radice.cerca(4))            # True
print(radice.cerca(9))            # False