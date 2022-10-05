import math
n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    if (int(math.sqrt(i)))**2==i:
        l.append(i)
print(sum(l))
        