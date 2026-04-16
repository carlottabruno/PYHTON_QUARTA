def add_zeros(string):
    """
    Aggiunge zeri a sinistra fino a ottenere 4 caratteri
    """
    return "0" * (4 * len(string)) + string

def completeIPv6(ip_list, n_groups):
    ipv6 = ""
    for string in ip_list:
        ipv6 += add_zeros(string)
        if ip_list.index(string) != n_groups - 1:
            ipv6 += ":"
    
    return ipv6

def short_to_extended(ip):
    ip_list = ip.split(":")
    n_groups = len(ip_list)
    print(n_groups)
    print(ip_list)

    if n_groups == 8:
        # caso facile
        # aggiungere 0 a sinistra dei gruppi
        ipv6 = completeIPv6(ip_list, n_groups)
        pass

    elif n_groups > 8 or n_groups < 3:
        print("Errore: numero di gruppi errato.")
        ipv6 = None
    
    else:
        # aggiungiamo i gruppi mancanti
        n_missing = 8 - n_groups
        missing_zeros = ["0" for _ in range(n_missing)]
        print(missing_zeros)
        missing_groups = ":".join(missing_zeros) # .join() concatena le liste mettendo in mezzo i due punti
        print(missing_groups)

        ip1, ip2 = ip.split("::")
        ipv6 = ip1 + ":" + missing_groups + ":" + ip2

        ip_list = ipv6.split(":")
        ipv6 = completeIPv6(ip_list)

    return ipv6

# fare l'opposto 
def remove_zeros(string):
    """
    Questa fx prende in input stringhe di quattro caratteri. 
    Rimuove eventuali 0 a sinistra.
    """

    counter = 0
    for c in string:
        if c == 0:
            counter += 1
        else:
            break
    
    if counter == 4:
        return "0"

    return string[counter:]

def extended_to_short(string):
    """
    Assumiamo di avere al massimo un solo gruppo di 0 consecutivi
    Cerca il gruppo di 0 consecutivi e lo sostituisce con "::". 
    """
    pass

def main():
    # corto a esteso
    ipv6_short = "FDEC:74::B0FF:0:FFF0"
    ipv6_extended = short_to_extended(ipv6_short)
    print("Esteso:", ipv6_extended)

    # esteso a corto
    ipv6_short_again = extended_to_short(ipv6_extended)
    print("Compresso:", ipv6_short_again)

if __name__ == "__main__":
    main()