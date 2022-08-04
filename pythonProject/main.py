
def print_hi(name):
    parola=input("Inserisci una parola ")
    while True:
        if parola=='chupacabra':
            break
        else:
            parola = input("Inserisci una parola ")
    print("Hai lasciato il ciclo con successo!")
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('PyCharm')


