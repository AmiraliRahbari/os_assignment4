def zarb(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
                print(str(i*j)+"    ",end='')
        print("\n")
                
n=int(input("please enter a number:"))
m=int(input("please enter a number:"))
zarb(n,m)

