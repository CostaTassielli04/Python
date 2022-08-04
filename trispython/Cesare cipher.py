def Cifratura(n): # questa funzione mi permette di crittografare la parola inserita da tastiera
    global cipher
    global messaggio #dichiaro queste variabili come globali ,in modo di averle sempre aggiornate
    for conta in range(n): #ripeto tutto fino a n shift, pk ogni volta che lo faccio shifto di 1
        cipher = ''
        for char in messaggio:
            if not char.isalpha():
                cipher += char #se è un numero oppure uno spazio bianco lo ricopio
                continue
            code = ord(char) + 1 #altrimenti aumento di uno il suo punto di codice ASCII
            if code > ord('Z') and char.isupper(): # se è più grande di Z o z lo ripristino ad a
                code = ord('A')
            elif code > ord('z') and char.islower():
                code = ord('a')
            cipher += chr(code) #mi costruisco la mia frase-parola crittografata
        messaggio=cipher #aggiorno il messaggio per la prossima crittografia

conta=0
messaggio=input("Inserisci il testo da crittografare: ")
shift=26
while shift>25:
    shift=int(input("Inserisci il numero di spostamenti: "))
print("Il messaggio",messaggio," crittogrfato di ",shift," ",end="")
Cifratura(shift)
print(cipher)