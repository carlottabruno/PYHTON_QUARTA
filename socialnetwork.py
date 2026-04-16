# SOCIAL NETWORK (rete di utenti)

class Rete():
    def __init__(self):
        self.utenti = [] 
    
    def iscrivi_utente(self, utente): # utente è un oggetto di tipo Utente
        self.utenti.append(utente)
        return utente
    
    def __str__(self):
        return f"N. utenti iscritti: {len(self.utenti)}"
    
    def aggiungi_amicizia(self, utente1, utente2):
        # crea amicizia tra utente1 e utente2
        if utente1 in self.utenti and utente2 in self.utenti:
            utente1.aggiungi(utente2)
            utente2.aggiungi(utente1)
        else: 
            # creare gli utenti che non esistono
            print("Almeno uno dei due utenti non è iscritto alla rete.")
    
    def amici_in_comune(self, utente1, utente2):
        # restituisce la lista degli amici in comune tra utente1 e utente2
        # si tratta di una lista di Utenti!
        lista_amici_comuni = []
        for amico in utente1.amici:
            if amico in utente2.amici:  
                lista_amici_comuni.append(amico)
        
        return lista_amici_comuni

    # def suggerisci_amici(self, utente):
    #    suggeriti = []

    #    for amico in utente.amici:
    #        for a in amico.amici:
    #            if a not in utente.amici and a != utente:  
    #                suggeriti.append(a)
        
        # cerco i doppioni in suggeriti e questi sono gli amici suggeriti, stampo solo se sono doppioni
        
    #    return suggeriti

    def suggerisci_amici(self, utente):
        suggeriti = []

        for amico in utente.amici:
            for a in amico.amici:
                if a not in utente.amici and a != utente:  
                    suggeriti.append(a)
        
        # devono essere doppioni
        amici_suggeriti = []
        for u in suggeriti:
            if u not in amici_suggeriti:
                volte = 0
                for s in suggeriti:
                    if s == u:
                        volte = volte + 1
                if volte > 1:
                    amici_suggeriti.append(u)
        
        return amici_suggeriti
    
    def carica_da_file(self, file_nome):
        file = open(file_nome, "r")
        righe = file.readlines()
        file.close()

        lista_persone = []
        lista_lista = []

        for riga in righe:
            lista_amici = []
            fields = riga.split(":")
            nome_persona = fields[0] 

            lista_persone.append(nome_persona)

            parti_lista = fields[1].split(",")
            lista_amici.append(parti_lista)

            lista_lista.append(lista_amici)

            self.iscrivi_utente(Utente(nome_persona))

        for lista, nome in zip(lista_lista, lista_persone):
            for amico in lista:
                self.aggiungi_amicizia(nome, amico)

class Utente():
    def __init__(self, nome):
        self.nome = nome
        self.amici = [] # lista di oggetti Utente

    def aggiungi(self, utente):
        self.amici.append(utente)
    
    def __str__(self):
        # stampa utente e i suoi contatti
        lista_nomi = [amico.nome for amico in self.amici] # list comprehension!

        return f"Nome: {self.nome}, Amici: {lista_nomi}"
    
def stampa_nomi(lista):
    lista_nomi = [utente.nome for utente in lista]
    return f"{lista_nomi}" 

def main():
    social_network = Rete()

    luca = Utente("Luca")
    mario = Utente("Mario")
    lucia = Utente("Lucia")

    social_network.iscrivi_utente(luca)
    social_network.iscrivi_utente(mario)
    social_network.iscrivi_utente(lucia)

    print(social_network)

    social_network.aggiungi_amicizia(luca, mario)
    print(mario)
    print(luca)

    social_network.aggiungi_amicizia(mario, lucia)
    print(mario)
    print(lucia)

    lista = social_network.amici_in_comune(luca, lucia)
    print(f"Gli amici in comune sono: {[u.nome for u in lista]}")

   # lista_suggeriti = social_network.suggerisci_amici(luca)
   # print(f"Gli amici suggeriti sono: {[u.nome for u in lista_suggeriti]}")

    lista_suggeriti = social_network.suggerisci_amici(luca)
    print(f"Gli amici suggeriti sono: {[u.nome for u in lista_suggeriti]}")


    social_network.carica_da_file("./utenti.txt")
    print(social_network)

if __name__ == "__main__": 
    main()