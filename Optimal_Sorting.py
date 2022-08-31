n=int(input())
a=0
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    m=sorted(l)
    if l==m:
        print(0)
    else:
        print(m[-1]-m[0])
        