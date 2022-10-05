import math
n=int(input())
k=list(map(int,input().split()))
l=[]
s=math.ceil(n/2)
a=k[:s]
b=k[s:]
for i,j in zip(a,b[::-1]):
    l.append(i)
    l.append(j)
if n%2==0:
    print(*l)
else:
    l.append(a[-1])
    l.append(0)
    print(*l)

    