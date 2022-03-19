from random import randrange

def display_board(board):
    # La funzione accetta un parametro contenente lo stato attuale della scheda
    # e lo stampa sulla console.

    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for j in range(3):
            print("|  ", board[i][j], end="   ")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def victory_for(board, sign):
    # La funzione analizza lo stato della scheda per verificare se
    # il giocatore che usa le "O" o le "X" ha vinto la partita

    conta=0
    global cond
    for i in range(3):
        for j in range(3):      # riga
            if board[i][j]==sign:
                conta=conta+1
        if conta==3:
            print("Il giocatore che usa ",sign," ha vinto questo match!")
            cond=False
            return
        conta=0

    conta=0
    for i in range(3):
        for j in range(3):
            if i==j:                 #obliquo 1
                if board[i][j]==sign:
                    conta=conta+1
    if conta == 3:
        print("Il giocatore che usa ", sign, " ha vinto questo match!")
        cond = False
        return

    conta=0
    i=0
    for j in range(2,-1,-1):                 #obliquo 2
        if board[i][j]==sign:
            conta=conta+1
        i=i+1
    if conta == 3:
        print("Il giocatore che usa ", sign, " ha vinto questo match!")
        cond = False
        return

    conta = 0
    for j in range(3):
        for i in range(3):                                        # colonna
            if board[i][j] == sign:
                conta = conta + 1
        if conta == 3:
            print("Il giocatore che usa ", sign, " ha vinto questo match!")
            cond = False
            return
        conta = 0

    conta=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X' or board[i][j]=='O':
                conta=conta+1
    if conta==9:
        print("La partita termina con un pareggio")
        cond=False
        return

def enter_move(board):
    # La funzione accetta lo stato attuale della scheda, chiede all'utente la sua mossa,
    # controlla l'input e aggiorna la scheda in base alla decisione dell'utente.
    simbolo='O'
    counter=0
    mossa=int(input("Inserisci la tua mossa(posizione in cui mettere la O)"))
    if mossa<0 or mossa>10:
        enter_move(board)
    else:
        for k in range(3):
            for x in range(3):
                if board[k][x]==mossa:
                    board[k][x]=simbolo
                else:
                    counter+=1
                if counter == 9:
                    enter_move(board)

                    break

    victory_for(board,simbolo)

def make_list_of_free_fields(board):
    # La funzione esplora il tabellone e costruisce un elenco di tutte le caselle libere;
    # l'elenco è composto da tuple, mentre ogni tupla è una coppia di numeri di riga e di colonna.

    elenco = []
    for i in range(3):
        for j in range(3):
            if board[i][j]!='X'or board[i][j]!='0':
                tupla=(i,j)
                elenco.append(tupla)
    return elenco

def draw_move(board):
    # La funzione disegna la mossa del computer e aggiorna la scheda.
    simb='X'
    counter=0
    list=make_list_of_free_fields(board)
    index=randrange(len(list))
    tuple=list[index]
    row=tuple[0]
    column=tuple[1]
    if board[row][column]=='X' or board[row][column]=='O':
        for i in range(3):
            for j in range(3):
                if board[row][column] == 'X' or board[row][column] == 'O':
                    counter=counter+1
        if counter==9:
            victory_for(board,simb)


        draw_move(board)
    else:
        board[row][column]='X'
    display_board(board)
    victory_for(board,simb)

n=1
cond=True
board=[[0 for j in range(3)]for i in range(3)]
for i in range(3):
    for j in range(3):
        board[i][j]=n
        n+=1
board[1][1]='X'
display_board(board)
while cond==True:
    print("##################################################################","\n")
    enter_move(board)
    if cond==False:
        break
    print("##################################################################", "\n", "Mossa del pc...")
    draw_move(board)
