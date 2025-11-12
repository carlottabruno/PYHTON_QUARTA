# assegni alla variabile lista_voti una lista con tutti i voti (almeno 6)
# sfrutta indicizzazione per: stampare la lista senza primo e ultimo voto
# sostituire il 4^ voto con un 10
# stampare i primi 3 voti della lista

lista_voti = [5, 7, 9, 3, 5, 4, 2]

for voto in lista_voti[1:6]:
    print(voto, end=" ")  
print(f" ")

lista_voti[4] = 10

print(f"sostituire il 4^ voto con un 10 ")
for voto in lista_voti:
    print(voto, end=" ")
print(f" ")

print(f"stampare i primi 3 voti della lista ")
for voto in lista_voti[0:3]:
    print(voto, end=" ")



