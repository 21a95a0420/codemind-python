n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
m=0
for i in k:
    if  a<=i<=b:
        l.append(i)
        m=1
if m==0:
    print(-1)
else:
    print(*l)