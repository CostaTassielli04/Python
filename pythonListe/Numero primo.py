def verifica_primo(n):
    conta=0
    for j in range(1,n+1):
        if(n%j==0):
            conta+=1
    if(conta<=2):
        return True
    else:
        return False


for i in range(1,20):
    if verifica_primo(i+1):
        print(i+1,end=" ")
