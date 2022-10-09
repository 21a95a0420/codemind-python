m,n=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
s=0
for i in x:
    s+=sum(i)
print(s)