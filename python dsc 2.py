def lists_():
    l=eval(input("enter a array:"))
    h=[]
    for i in l:
        if i in h:
            continue
        else:
            h.append(i)
    print("array after removing duplicates:",h)
lists_()
