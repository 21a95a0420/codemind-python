def did(x):
    l=len(str(x))-1
    s=0
    while x:
        s+=(x%10)*(10**l)
        x=x//10
        l=l-1
    return(s)
n=int(input())
if n<0:
    print(-1*did(abs(n)))
else:
    print(did(n))