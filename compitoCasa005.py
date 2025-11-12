# realizzare un programma python che converta un indirizzo ip in una stringa binaria di 32 bit

ip = input("Inserisci un indirizzo IP: ")

ottetti_str = ip.split(".")

print(ottetti_str)

ottetti_bin = []

for o in ottetti_str:
    n = int(o)
    b = bin(n)[2:]

    if len(b) < 8:
        b = "0" * (8 - len(b))
    ottetti_bin.append(b)

ip_binario = ""
for b in ottetti_bin:
    ip_binario = ip_binario + b

print("Ottetti originali:", ottetti_str)
print("Ottetti in binario:", ottetti_bin)
print("Stringa binaria di 32 bit:", ip_binario)