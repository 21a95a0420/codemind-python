def op(a):
    k,l=0,a
    while a:
        r=a%10
        a//=10
        if r!=0:
            if l%r==0:
                k+=1
    return k==len(str(l))
n=int(input())
m=int(input())
for i in range(n,m+1):
    if op(i):
        print(i,end=' ')
