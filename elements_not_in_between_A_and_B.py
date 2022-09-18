n=int(input())
kal=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in kal:
    if i<a or i>b:
        k.append(i)
if len(k)==0:print(-1)
else:print(*k)