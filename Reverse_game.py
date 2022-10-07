n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    m=str(i)
    o=m[::-1]
    l.append(int(o))
print(*l)