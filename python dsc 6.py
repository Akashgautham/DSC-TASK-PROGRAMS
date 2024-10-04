def sum_of_list(lst):
    print("sum:", sum(lst))
def max_min_list(lst):
    print("max and min:", max(lst), min(lst))
def reverse_list(lst):
    print("Reversed list:", lst[::-1])
def second_largest(lst):
    l=len(lst)
    top=l-2
    lst.sort()
    print("second largest:",lst[top])
def is_palindrome(lst1,lst2):
    if lst1 == lst2[::-1]:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
def find_index(lst, element):
    if element in lst:
        print("index:", lst.index(element))
    else:
        print("not found")

lst=eval(input("enter a list:"))
print("""1.sum of elements
2.max and min of list
3.reverse list
4.second largest
5.check for palindrome""")
ans='y'
while ans=='y':
    ch=int(input("Enter your choice:"))
    if ch==1:
        sum_of_list(lst)
    elif ch==2:
        max_min_list(lst)
    elif ch==3:
        reverse_list(lst)
    elif ch==4:
        second_largest(lst)
    elif ch==5:
        lst1=eval(input("enter list 1:"))
        lst2=eval(input("enter list 2:"))
        is_palindrome(lst1,lst2)
    else:
        print("invalid choice:")
    ans=input("do you want to continue[y/n]:")
        
    

        
        
