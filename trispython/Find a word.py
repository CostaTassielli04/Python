def CercaSottostringa(f,p):
    f=f.lower()
    p=p.lower()
    n=f.find(p)
    return n
frase=input("Inserisci una frase/parola: ")
parola=input("Inserisci una parola da cercare all'interno della frase: ")
j=CercaSottostringa(frase,parola)
if j==-1:
    print("La sottostringa non è presente nella frase ")
else:
    print("La sottostringa è presente nella frase ")
