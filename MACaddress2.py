def main():
    file = open("./macvendors.csv", "r", encoding = 'utf-8')
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []
    data_produzione = []

    for riga in righe[1:]:
        campi = riga.split(",")
        mac_address.append(campi[0])
        vendor.append(campi[1])
        data_produzione.append(campi[4])

    # exit() # esclude la parte sottostante di programma

    mac = "44:FA:66:37:57:C5"

    for m, v, d in zip(mac_address, vendor, data_produzione):
        if m == mac[0:8]:
            print(f"Il produttore è {v}")
            print(f"La data di produzione è {d}")

if __name__=="__main__":
    main()

# stampare anche la data di produzione, modificando il codice