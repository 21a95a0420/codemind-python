n=int(input())
kal=list(map(int,input().split()))
kal=sorted(kal)
k=[]
a=0
for i in kal:
    a=i*i
    k.append(a)
print(*sorted(k))
    