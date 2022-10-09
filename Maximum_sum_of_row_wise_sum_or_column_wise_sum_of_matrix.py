m,n=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
a=0
z=[]
for i in range(n):
    for j in range(m):
        a+=x[j][i] 
    z.append(a)
    a=0
for i in x:z.append(sum(i))
print(max(z))