import math

n = int(input("Inserisci un numero: "))
somma = 0

for i in range(1, 2 * n + 1, 2):
    somma += i

radiceIntera = math.isqrt(somma)

print(f"La somma è {somma}. Quadrato perfetto: {radiceIntera**2 == somma}")

if somma == n**2:
    print("E' un quadrato perfetto")
else:
    print("Non è un quadrato perfetto")