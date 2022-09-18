n=int(input())
kal=list(map(int,input().split()))
c=0
for i in kal:
    if i in [1,0]:
        c+=1
print(c==n)