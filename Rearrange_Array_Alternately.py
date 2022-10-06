import math
n=int(input())
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    s=math.ceil(len(l)/2)
    m=l[:s]
    n=l[s:]
    o=[]
    for i,j in zip(m,n[::-1]):
        o.append(j)
        o.append(i)
    if len(l)%2==0:
        print(*o)
    else:
        o.append(m[-1])
        print(*o)