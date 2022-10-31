n=int(input())
k=list(map(int,input().split()))
p=1
for i in k:
    p*=i
z=[]
for i in k:
    z.append(p//i)
print(*z)