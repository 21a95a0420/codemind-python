n=int(input())
k=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in k:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
for i,j in zip(range(len(a)),range(len(b))):
    c.append(a[i])
    c.append(b[j])
j=abs(len(a)-len(b))
if len(a)>len(b):
    y=a[-j:]
    for i in y:
        c.append(i)
if len(a)<len(b):
    y=b[-j:]
    for i in y:
        c.append(i)
if len(c)%2!=0:
    c.append(0)
    print(*c)
else:
    print(*c)
    