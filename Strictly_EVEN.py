n=int(input())
kal=list(map(int,input().split()))
c=0
d=0
for i in range (len(kal)):
    if kal[i]%2==0:
        c+=1
        if i%2==0:
            d+=1
        else:
            break
if c==d:
    print('True')
else:
    print('False')