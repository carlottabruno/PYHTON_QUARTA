import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket

    DESTINATARIO = ("192.168.1.108", 13000) # è un processo
    messaggio = input("-> ") # stringa

    s.sendto(messaggio.encode(), DESTINATARIO)

    while True:
        dati, ip_porta_mittente = s.recvfrom(4096) 
        stringa = dati.decode() # trasforma i dati binari in stringa
        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")

        if stringa.upper() == "EXIT":
            break

    s.close()

if __name__ == "__main__":
    main()