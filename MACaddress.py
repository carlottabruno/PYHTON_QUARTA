# chiede in input il mac address, apre il file, leggerlo, 
# fare una ricerca sulle righe dei primi 3 byte così si trova
# scrivere un programma che rileva il vendor associato a un MAC address

def main():
    # macAddress = input("Inserisci il MAC Address: ")
    mac = "E4:60:17"
    # mac = macAddress.split(":")

    file = open("./macvendors.csv", "r", encoding = 'utf-8') 
    # utf-8 risolve i problemi dell'apertura del file

    righe = file.readlines() 
    file.close()

    for i in righe:
        if mac == i[0:8]:
            print(i)
            print(f"Vendor: {i}")

if __name__=="__main__":
    main()