def prime(x):
    s=0
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            s+=1
    return (s==0)
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i)==True:
        print(i)
        