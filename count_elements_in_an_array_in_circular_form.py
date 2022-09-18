n=int(input())
kal=list(map(int,input().split()))
kal.append(kal[0])
kal.append(kal[1])
c=0
for i in range(1,n+1):
    if kal[i+1]%2==0 and kal[i-1]%2==1:
        c+=1
    if kal[i+1]%2==1 and kal[i-1]%2==0:
        c+=1
print(c)