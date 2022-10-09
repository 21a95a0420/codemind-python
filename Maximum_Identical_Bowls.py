n=int(input())
k=list(map(int,input().split()))
l=sum(k)
for i in range(n,0,-1):
    if l%i==0:
        print(i)
        break