def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def mok(k):
    b=str(k)
    c=0
    for i in range(len(b)):
        a=k%10
        k=k//10
        if prime(a)==True:
            c+=1
    return(c)
n=int(input())
s=str(n)
if prime(n)==True and mok(n)==len(s):
    print('Mega Prime')
else:
    print('Not Mega Prime')
