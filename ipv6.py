ip = input("Inserisci IPv6: ")

doppio = False
for i in range(len(ip) - 1):
    if ip[i] == ":" and ip[i+1] == ":":
        doppio = True

if doppio:
    parti = ip.split("::")

    if parti[0] != "":
        sx = parti[0].split(":")
    else:
        sx = []

    if len(parti) > 1 and parti[1] != "":
        dx = parti[1].split(":")
    else:
        dx = []

    mancanti = 8 - (len(sx) + len(dx))
    gruppi = sx + ["0"] * mancanti + dx
else:
    gruppi = ip.split(":")

completo = ""
for i in range(len(gruppi)):
    g = gruppi[i]

    while len(g) < 4:
        g = "0" + g

    completo = completo + g
    if i < len(gruppi) - 1:
        completo = completo + ":"

abbrev = ""
parti = completo.split(":")

for i in range(len(parti)):
    g = parti[i]

    while len(g) > 1 and g[0] == "0":
        g = g[1:]

    abbrev = abbrev + g
    if i < len(parti) - 1:
        abbrev = abbrev + ":"

print(f"Completo: {completo}")
print(f"Abbreviato: {abbrev}")