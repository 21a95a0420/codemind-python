def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def rev(n):
    k=0
    while n:
        r=n%10
        k=k*10+r
        n=n//10
    return k
n=int(input())
b=rev(n)
if prime(n)==True:
    if prime(b)==True:
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')