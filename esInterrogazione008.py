m = "A0-FF-51-B3-D1-FF"

m2 = m.split("-")

for i in m2:
    if i != "FF":
        print(i, end=" ")