m,n=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
z=[]
for i in x:
    z.append(sum(i))
print(max(z))