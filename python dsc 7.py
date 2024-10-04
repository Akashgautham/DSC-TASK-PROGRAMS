def sort_dict_by_keys(d):
    print("sorted:",dict(sorted(d.items())))

def max_min_dict(d):
    max_value = max(d.values())
    min_value = min(d.values())
    print("max and min:", max_value, min_value)

def remove_key(d, key):
    if key in d:
        del d[key]
    print("deleted:", d)

def sum_values(d):
    print("sum of values:", sum(d.values()))

def update_dict(d1, d2):
    d1.update(d2)
    print("updated dict:", d1)
n=int(input("number of entries:"))
d={}
for i in range(n):
    key=input("enter key:")
    value=int(input("enter value:"))
    d[key]=value
print("""1.sort
2.max and min
3.remove key
4.sum
5.update""")
ans='y'
while ans=="y":
    ch=int(input("enter your choice:"))
    if ch==1:
        sort_dict_by_keys(d)
    elif ch==2:
        max_min_dict(d)
    elif ch==3:
        key=input("enter key to be removed:")
        remove_key(d, key)
    elif ch==4:
        sum_values(d)
    elif ch==5:
        d1=eval(input("enter dict1:"))
        d2=eval(input("enter dict2:"))
        update_dict(d1, d2)
    else:
        print("invalid choice")
    ans=input("do you want to continue[y/n]:")
    
        
        
