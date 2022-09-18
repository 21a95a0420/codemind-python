n=int(input())
kal=list(map(int,input().split()))
k=[]
for i in kal:
    k.append(len(str(abs(i))))
print(*k)
    