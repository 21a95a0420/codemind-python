n=int(input())
k=list(map(int,input().split()))
l=0
for i in k:
    m=str(i)
    if m==m[::-1]:
        l+=1
print(l)