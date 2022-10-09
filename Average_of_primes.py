def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    if prime(i):
        l.append(i)
print('{:.2f}'.format(sum(l)/len(l)))