def prime(x):
    if n==1:return False
    for i in range(2,x):
        if x%i==0:return False
    return True
n=int(input())
s=0
if prime(n):
    while n:
        if prime(n%10)==False:
            print('Not Mega Prime')
            s=1
            break
        n//=10
    if s==0:print('Mega Prime')
else:print('Not Mega Prime')