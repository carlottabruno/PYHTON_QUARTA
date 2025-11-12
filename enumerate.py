def main_0():
    lista = ["Alice", "Luca", "Giovanni", "Mario"]
    nome_max = None
    # if nome_max: questa if è falsa perchè nome_max = None
    len_max = 0
    for nome in lista:
        if len(nome) > len_max:
            len_max = len(nome)
            nome_max = nome
    print(nome_max)

def main_1():
    lista = ["Alice", "Luca", "Giovanni", "Mario"]
    
    for i, nome in enumerate(lista):
        print(f"{i} - {nome}")

if __name__=="__main__": # dunder = double underscore
    main_0()
    main_1()

    print(__name__) # con dunder sono variabili private
# questa if è vera solo se eseguo il programma
