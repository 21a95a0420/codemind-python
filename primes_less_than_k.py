def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=int(input())
k=list(map(int,input().split()))
c=int(input())
l=0
for i in k:
    if i<=c and prime(i):
        l+=1
print(l)
        
