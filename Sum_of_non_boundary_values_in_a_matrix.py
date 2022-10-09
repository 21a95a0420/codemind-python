m,n=map(int,input().split())
x=[]
for i in range(m):
    x.append(list(map(int,input().split())))
c=0
for i in range(m):
    for j in range(n):
        if i!=0 and j!=0 and j!=n-1 and i!=m-1:
            c+=x[i][j]
print(c)