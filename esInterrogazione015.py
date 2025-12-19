def main():
    ip = input("Inserisci un ip: ")
    print(f"E' uguale a 4: {controlla(ip)}")

def controlla(ip):
    fields = ip.split(".")
    return len(fields) == 4

if __name__ == "__main__":
    main()