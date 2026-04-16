import socket

BUFFER_SIZE = 4096
IP_PORTA = ("127.0.0.1", 13000) # THIS HOST

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket

    s.bind(IP_PORTA) # metodo per legare

    print("Server in ascolto...")

    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE) # riceve dalla scheda di rete e mette dentro un buffer, E' BLOCCANTE!!!
        stringa = dati.decode() # trasforma i dati binari in stringa
        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")

        s.sendto(dati, ip_porta_mittente)

        if stringa.upper() == "EXIT":
            break

    s.close() # chiude il socket

if __name__ == "__main__":
    main()