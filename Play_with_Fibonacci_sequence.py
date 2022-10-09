n=int(input())
x=[0,1]
a=0
b=1
for i in range(n-2):
    c=a+b
    a,b=b,c
    x.append(c)
print(*x)