n=int(input())
kal=list(map(int,input().split()))
k=sum(kal)//n
c=0
for i in kal:
    if i<k+1:
        c+=1
print(c)
