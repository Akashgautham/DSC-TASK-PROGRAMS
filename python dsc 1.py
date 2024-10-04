def string_asc():
    string=input("enter a string:")
    lists=[]
    lists=string.split()
    lists2=sorted(lists,key=len)
    print("sorted string:",lists2)
string_asc()
            
