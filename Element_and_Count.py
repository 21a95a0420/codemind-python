n=int(input())
k=list(map(int,input().split()))
l=[]
m=[]
a=[]
for i in k:
    if i not in l:
        l.append(i)
for i in l:
    m.append(k.count(i))
for i,j in zip(l,m):
    a.append(i)
    a.append(j)
print(*a)
    