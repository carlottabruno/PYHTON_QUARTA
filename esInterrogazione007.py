def oscura(s):
    return s[0] + len(s) * '*'

lista = ["ciao", "unoduetre"]

lista2 = ""

for i in lista:
    lista2 = lista2 + oscura(i)

print(lista2)