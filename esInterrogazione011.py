def trova(m1, m2):
    g1 = m1.split("-")
    g2 = m2.split("-")
    cont = 0

    for g1, g2 in zip(m1, m2):
        if g1 == g2:
            cont += 1
    
    return cont

def main():
    m1 = "A0-FF-51-B3-D1-FF"
    m2 = "A0-FF-51-B3-D1-FF"
    print(trova(m1, m2))

if __name__=="__main__":
    main()