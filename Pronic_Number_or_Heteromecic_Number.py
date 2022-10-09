n=int(input())
k=[]
for i in range(1,n+1):
    if n%i==0:
        k.append(i)
for i in range(len(k)-1):
    if k[i]*k[i+1]==n and k[i]+1==k[i+1]:
        print('YES')
        break
else:
    print('NO')