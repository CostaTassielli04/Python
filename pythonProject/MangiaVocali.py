def print_hi(name):

    parola=input("Inserisci una parola ")
    parola=parola.upper()
    stringa=""

    for letter in parola:
        if letter=='A':
            continue
        elif letter=='E':
            continue
        elif letter=='O':
            continue
        elif letter=='I':
            continue
        elif letter=='U':
            continue
        else:
            stringa+=letter
    print(stringa)
if __name__=='__main__':
    print_hi('PyCharm')