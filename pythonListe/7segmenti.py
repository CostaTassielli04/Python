#Hai sicuramente visto un display a sette segmenti.

#È un dispositivo (a volte elettronico, a volte meccanico) progettato per presentare una cifra decimale utilizzando un sottoinsieme di sette segmenti. Se ancora non sai di cosa si tratta, fai riferimento al seguente articolo di Wikipedia.

#Il tuo compito è scrivere un programma in grado di simulare il lavoro di un dispositivo a sette display, anche se utilizzerai LED singoli anziché segmenti.

#Ogni cifra è composta da 13 LED (alcuni accesi, altri scuri, ovviamente)

def settesegmenti(cifre,lista):
    for char in cifre:
        if char=="0":
            lista[0][0],lista[0][1],lista[0][2],lista[1][0],lista[1][2],lista[2][0],lista[2][2],lista[3][0],lista[3][2],lista[4][0],lista[4][1],lista[4][2]="#"
            print(lista)
            lista.clear()


lista=[[" " for i in range(3)]for j in range(5)]
cifre=input("Inserisci una serie di cifre")
settesegmenti(cifre, lista)