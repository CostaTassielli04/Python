

def print_hi(name):
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    my_list2=my_list[:]
    for i in my_list2:
        if i in my_list2:
            del my_list2[i]

    my_list=my_list2
    print("The list with unique elements only:")
    print(my_list)


if __name__=='__main__':
    print_hi("PyCharm")
