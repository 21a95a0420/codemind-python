n=int(input())
k=list(map(int,input().split()))
if n%2==0:
    print(*k)
else:
    k.append(0)
    print(*k)
