n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in lst:
    if lst.count(i)==i:
        if i in a:
            continue
        a.append(i)
if len(a)>0:
    k=sum(a)/len(a)
if len(a)==0:
    print(-1)
else:
    print('{:.2f}'.format(k))
            