def shatranj(n,m):
    for i in range(n):
        for j in range(0,m,2):
            if i%2==0:
                print("#*",end='')
            else:
                print("*#",end='')
        print("\n")
                
n=int(input("please enter a number:"))
m=int(input("please enter a number:"))
shatranj(n,m)

