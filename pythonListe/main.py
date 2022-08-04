
def print_hi(name):
    cappello_lista=[1,2,3,4,5]

    n=int(input("Inserisci un nuovo numero"))
    cappello_lista[2]=n

    del cappello_lista[-1]

    print("La lunghezza attuale della lista: ", len(cappello_lista))
    print("La lista: ",cappello_lista)

    my_list = ["white", "purple", "blue", "yellow", "green"]

    for color in my_list:
        print(color)

        my_list = [8, 10, 6, 2, 4]  # list to sort

        for i in range(len(my_list)):
            for j in range(i + 1, 5, 1):
                if my_list[i] > my_list[j]:
                    my_list[i], my_list[j] = my_list[j], my_list[i]

        print(my_list)

        squares = [x ** 2 for x in range(10)]
        print(squares)
        odds = [x for x in squares if x % 2 != 0 ]
        print(odds)

        print("O")
        vals=[1,2,3]
        for i in range(len(vals)):
            vals.insert(1,vals[i])

        print (vals)
        var=0
        while var<6:
            var+=1
            if var%2==0:
                continue
            print('#')

if __name__ == '__main__':
    print_hi('PyCharm')
