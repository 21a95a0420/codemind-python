def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
a=int(input())
c=2
for i in range(2,int(a/2)+1):
    if a%i==0 and prime(i)==False:
        c+=1
print(c)