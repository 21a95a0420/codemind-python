a,b=map(int,input().split())
k=list(map(int,input().split()))
l=list(map(int,input().split()))
x=k+l
o=[]
for i in k:
    if i not in o and i in l:
        o.append(i)
print(*o)