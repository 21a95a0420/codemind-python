n,a=map(int,input().split())
k=list(map(int,input().split()))
c=0
for i in k:
    if i%a==0:
        c+=1
print(c)