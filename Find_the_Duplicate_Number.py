n=int(input())
k=list(map(int,input().split()))
for i in  k:
    if k.count(i)>1:
        print(i)
        break