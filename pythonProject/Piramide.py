def print_hi(name):
    blocks=int(input("Inserisci il numero di blocchi"))
    height=0
    i=0
    while blocks>0:
        i += 1
        if blocks>1 and blocks>=i:
            blocks=blocks-i
            height=height+1
        else:
            break
    print("I blocchi sono terminati...")
    print("L'altezza della piramide: ",height)
print_hi('Ciao ')
