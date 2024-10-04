stk=[]
def push(int1):
    stk.append(int)
    print("inserted")
def pop():
    if stk==[]:
        print("stack empty")
    else:
        print("Popped element:",stk.pop())
def peek():
    top=len(stk)-1
    print(stk[top])
print("""1.push
2.pop
3.peek""")
ans='y'
while ans=='y':
    ch=int(input("Enter your choice:"))
    if ch==1:
        int1=int(input("enter the number to be pushed:"))
        push(int1)
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    else:
        print("invalid choice")
    ans=input("do you want to continue[y/n]:")
    
