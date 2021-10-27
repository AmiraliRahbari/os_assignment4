n=int(input("please enter n:"))
f0=0;f1=1
list=[f0,f1]
for i in range(n+1):
    f=f0+f1
    list.append(f)
    f0=f1
    f1=f

print(list)
