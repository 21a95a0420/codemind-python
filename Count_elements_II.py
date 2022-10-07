a,b=map(int,input().split())
k=list(map(int,input().split()))
l=list(map(int,input().split()))
m=set(k)
n=set(l)
o=[]
for i in m:
    if i not in n:
        o.append(i)
for j in n:
    if j not in m:
        o.append(j)
print(len(o))