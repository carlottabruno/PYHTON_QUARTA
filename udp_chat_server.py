import socket

IP_PORTA = ("localhost", 12345)
BUFFER_SIZE = 4096
SEPARATORE = "|"
LOG_LEVEL = "DEBUG"

def log(stringa, tipo):
    """
    Stringa = la stringa stampata in output
    Tipo = INFO | DEBUG | ERROR
    """
    if (tipo.upper() == "DEBUG") and (LOG_LEVEL == "DEBUG"):
        print(f"[DEBUG]: {stringa}")
    elif (tipo.upper() == "INFO") and (LOG_LEVEL == "INFO"):
        print(f"[INFO]: {stringa}")
    elif (tipo.upper() == "ERROR") and (LOG_LEVEL == "ERROR"):
        print(f"[ERROR]: {stringa}")

def main():
    # rubrica utenti
    rubrica = {}

    # creazione di un socket IPv4 e UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # lego socket a ip+porta
    s.bind(IP_PORTA)

    log(f"SERVER: indirizzo ip ({IP_PORTA[0]}), Porta ({ip_porta_mittente[1]})")

    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE)
        log(f"Ricevuto {dati.decode()} da {ip_porta_mittente}")

        # il server deve capire se il messaggio ricevuto è di HELLO, 
        # oppure di chat
        # se è un mess di hello, allora aggiorna la rubrica
        # se è di chat allora lo inoltra (DA NON FARE ANCORA)
        
        campi = dati.decode().split(SEPARATORE)
        dest, mess = campi

        if len(campi) == 2:
            dest, mess = campi
        else:
            log("ERRORE")
            continue
            
        if dest == "Server":
            if mess.upper() == "EXIT": break
            if mess not in rubrica:
                rubrica[mess] = ip_porta_mittente
                print(rubrica)
        
    s.close()

if __name__ == "__main__":
    main()