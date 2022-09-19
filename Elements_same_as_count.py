n=int(input()) 
kal=list(map(int,input().split()))
k=[]
y=[]
for i in kal:
    if i not in y:
        y.append(i)
for i in y:
    if kal.count(i)==i:
        k.append(i)
if len(k):
    print(*k)
else:
    print(-1)
        