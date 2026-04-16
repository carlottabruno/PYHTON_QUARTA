import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket

    DESTINATARIO = ("192.168.1.119", 15000) # è un processo
    messaggio = input("-> ") # stringa

    s.sendto(messaggio.encode(), DESTINATARIO)

    s.close() # chiude il socket

if __name__ == "__main__":
    main()