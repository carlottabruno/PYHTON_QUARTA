import readline

file = open("./nomeFile", "r")
righe = file.readline()

for i in righe:
    if(righe[0] == '#'):
        print(righe)

file.close()