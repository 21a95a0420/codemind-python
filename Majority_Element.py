n=int(input())
k=list(map(int,input().split()))
for i in k:
    if k.count(i)> len(k)//2:
        print(i)
        break