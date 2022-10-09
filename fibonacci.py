n=int(input())
a=0
b=1
d=[]
for i in range(n):
    temp=a
    d.append(a)
    a=b
    b=temp+a
print(*d)
    