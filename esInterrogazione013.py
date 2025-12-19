nomi = ["Luca", "Mario", "Alice"]
voti = [8, 7, 10]

dizionario = {}

for n, v in zip(nomi, voti):
    dizionario[n] = v

print(dizionario["Alice"])