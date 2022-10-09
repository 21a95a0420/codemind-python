m,n=map(int,input().split())
x=[]
for _ in range(m):
    x.append(list(map(int,input().split())))
c=[]
t=[[z[i] for z in x]for i in range(len(x[0]))]
k=0
for i in t:
    if sorted(i)==i:k+=1
    else:
        v=sorted(i)
        v.reverse()
        if v==i:k+=1
print(k)