n=int(input())
a=0
b=1
i=1
c=[]
while i<=n:
    temp=a
    c.append(a)
    a=b
    b=temp+a
    i+=1
if n in c:
    print('True')
else:
    print('False')
    