# caricare su un dizionario mac address e vendor a partire dal file csv
# dei Mac address. Fare la ricerca del vendor usando il dizionario.

import uuid

def getMyMac():
    mac = uuid.getnode()
    mac_str = ':'.join(f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -1, -8)) 
    return mac_str

def preparaMac(mac_Str):
    mac_Str = mac_Str.replace("-", ":")
    return mac_Str.upper()

def main():
    file = open("./macvendors.csv", "r", encoding="utf-8")
    righe = file.readlines() # righe è una liste di stringhe
    file.close()

    elenco = {}

    for riga in righe[1:]:  # riga è una stringa
        campi = riga.split(",") # campi è una lista di stringhe 
        elenco[campi[0]] = campi[1]

    ricerca = "70:B3:D5:19:B"
  
    if ricerca in elenco:
        print(f"Vendor: {elenco[ricerca]}")
    else:
        print("Vendor non trovato")
    
    print(getMyMac().upper())
    primiTreByte = preparaMac(getMyMac().upper())[:8]
    myMacPreparato = preparaMac(getMyMac().upper())

    if primiTreByte in elenco:
        print(f"Il produttore {myMacPreparato} è {elenco[primiTreByte]}")
    else:
        print(f"Produttore ignoto.\n")

if __name__ == "__main__":
    main()