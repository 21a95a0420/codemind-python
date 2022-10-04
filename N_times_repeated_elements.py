a=int(input())
k=list(map(int,input().split()))
m=int(input())
a=[]
for i in k:
    if k.count(i)==m:
        if i in a:
            continue
        a.append(i)
if len(a)==0:
    print(-1)
if len(a)>0:
    print(*a)