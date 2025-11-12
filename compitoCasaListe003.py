# quadrati perfetti minori di 200

import math

somma = 0

for i in range(1, 200):
    if i == math.isqrt(i)**2:
        somma += 1

print(f"I quadrati perfetti sono {somma}")