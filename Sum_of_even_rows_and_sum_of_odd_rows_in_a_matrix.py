m,n=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
z=[]
b=0
a=0
for i in range(m):
    if i%2==0:a+=sum(x[i])
    else:b+=sum(x[i])
print(a,b)