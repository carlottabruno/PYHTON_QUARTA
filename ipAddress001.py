ip = input("Inserisci un indirizzo IP: ")

ottetti_str = ip.split(".") # .split(SEPARATORE) è un metodo delle stringhe che suddivide una stringa cercando il carattere separatore 

print(ottetti_str)

ottetti = [] # lista vuota

for s in ottetti_str:
	ottetti.append(int(s))
print(bin(ottetti[0])) # bin converte in una stringa binario