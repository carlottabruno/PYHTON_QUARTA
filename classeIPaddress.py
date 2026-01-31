class IPAddress():
    def __init__(self, ip, subnetmask):
        # ip è una stringa
        # subnetmask è una stringa /XX
        self.ip = ip
        self.subnetmask = subnetmask
    
    def networkAddress(self):
        # restituisce l'indirizzo di rete
        parti_ip = self.ip.split(".")
        subnetmask = int(self.subnetmask[1:])

        byte_rete = subnetmask // 8

        indirizzo_rete = ""

        for i in range(4):
            if i < byte_rete:
                indirizzo_rete = indirizzo_rete + parti_ip[i]
            else:
                indirizzo_rete = indirizzo_rete + "0"

            if i < 3:
                indirizzo_rete = indirizzo_rete + "."

        return indirizzo_rete
    
    def broadcastAddress(self):
        # restituisce l'indirizzo di broadcast
        parti_ip = self.ip.split(".")
        subnetmask = int(self.subnetmask[1:])

        byte_rete = subnetmask // 8

        indirizzo_broadcast = ""

        for i in range(4):
            if i < byte_rete:
                indirizzo_broadcast = indirizzo_broadcast + parti_ip[i]
            else:
                indirizzo_broadcast = indirizzo_broadcast + "255"

            if i < 3:
                indirizzo_broadcast = indirizzo_broadcast + "."

        return indirizzo_broadcast
    
    def hostNumber(self):
        # restituisce il numero di host
        return 2**(32 - int(self.subnetmask[1:])) - 2

def main():
    indirizzo = IPAddress("192.168.168.220", "/24")

    print(f"Indirizzo di rete: {indirizzo.networkAddress()}")
    print(f"Indirizzo di broadcast: {indirizzo.broadcastAddress()}")
    print(f"Numero di host: {indirizzo.hostNumber()}")

if __name__ == "__main__":
    main()