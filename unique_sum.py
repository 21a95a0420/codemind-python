n=int(input())
l=list(map(int,input().split()))
k=set(l)
c=0
for i in k:
    c+=i
print(c)