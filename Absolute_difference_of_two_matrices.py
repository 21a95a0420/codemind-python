n=int(input())
x=[list(map(int,input().split())) for i in range(n)]
y=[list(map(int,input().split())) for i in range(n)]
z=[]
a=[]
for i in range(n):
    for j in range(n):
        z.append(abs(x[i][j]-y[i][j]))
    a.append(z)
    z=[]
for i in a:
    print(*i)