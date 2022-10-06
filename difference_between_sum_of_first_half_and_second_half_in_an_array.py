n=int(input())
k=list(map(int,input().split()))
a=[]
b=[]
c=n//2
for i in range(c):
    a.append(k[i])
for j in k:
    if j not in a:
        b.append(j)
print(abs(sum(a)-sum(b)))