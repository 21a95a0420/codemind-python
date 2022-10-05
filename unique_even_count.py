n=int(input())
k=list(map(int,input().split()))
k=set(k)
l=0
for i in k:
    if i%2==0:
        l+=1
print(l)