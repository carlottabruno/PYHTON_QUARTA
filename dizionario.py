def main():
    # un dizionario è una sequenza di coppie chiave: valore
    elenco = {"A3-32-B4-FF-F4-32" : "Luca", 
              "65-A0-AA-11-F4-19" : "Mario"} # la prima parte si chiama CHIAVE e la seconda VALORE
    
    mac = "A3-32-B4-FF-F4-32"

    if mac in elenco:    
        print(elenco[mac])
    else:
        print(f"Mac non trovato\n")
    
    # aggiungiamo un nuovo elemento nel dizionario
    elenco["FF-FF-FF-FF-FF-FF"] = "broadcast"

    print(elenco)

if __name__=="__main__":
    main()


# dizionario = {} per dizionario vuoto