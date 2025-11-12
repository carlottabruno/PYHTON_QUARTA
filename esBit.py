# chiede numero di bit che vuole usare, chiede numero binario (gestire come stringhe), 
# se la lunghezza del numero bin inserito è minore del numero di bit 
# aggiungere a sinistra tanti zeri quanto bastano ad arrivare a 8

ip = input("Inserisci un indirizzo IP: ")

ottetti_str = ip.split(".") # .split(SEPARATORE) è un metodo delle stringhe che suddivide una stringa cercando il carattere separatore 

print(ottetti_str)

ottetti = [] # lista vuota

for s in ottetti_str:
	ottetti.append(int(s))
print(bin(ottetti[0])) # bin converte in una stringa binario




l = ["ciao", "python", "casa"]

stringa[0] = " "

for i in l:
	stringa = stringa + i

print(stringa)



nBit = int(input("Quanti bit vuoi usare? "))

numeroBin = input("Inserisci numero binario: ")

if len(bin) < nBit:
	


