def mysplit(strng):
    k=0
    char=''
    list=[]
    for i in strng:
        if i.isspace():
            if char=='':
                pass
            else:
                list.insert(k, char)
                char = ''
                k=k+1
        else:
           char= char+i
    if char !='' :
       list.insert(k, char) #ultima parola pk non c'è lo space

    return list
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
#for char in strng:if char.isspace():i=i+1else:list.insert(i,char)return list