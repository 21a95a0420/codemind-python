def pal(x):
    return str(x)[::-1]
n=int(input())
b=int(input())
for i in range(n,b+1):
    if pal(i)==str(i):
        print(i,end=' ')
        