n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in k:
    if i>=a and i<=b:
        l.append(i)
if len(l):
    print(max(l))
else:
    print(-1)