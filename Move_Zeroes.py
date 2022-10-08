n=int(input())
k=list(map(int,input().split()))
c=[]
s=[]
for i in k:
    if i!=0:
        c.append(i)
    elif i==0:
        s.append(i)
print(*(c+s))