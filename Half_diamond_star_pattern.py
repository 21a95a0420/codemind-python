n=int(input())
x=1
y=n-1
if n>=3:
    for i in range(n):
        for j in range(x):
            print("*",end="")
        x+=1
        print()
    for k in range(n-1):
        for i in range(y):
            print('*',end='')
        y-=1
        print()
else:
    print("The pattern is not possible")