n=int(input())
k=[]
while n>0:
    a=n%10
    k.append(a)
    n//=10
for i in k:
    if k.count(i)>1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')