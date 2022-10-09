m,n=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
b=0
a=0
for i in range(m):
    for j in range(n):
        if x[i][j]%2==0:
            a+=x[i][j]
        else:
            b+=x[i][j]
print(a,b)