def op(x):
    if x==0:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def k(n):
    a=n+1
    b=n-1
    while op(a)==False:
        a=a+1
    while op(b)==False:
        b=b-1
    if abs(n-a)>abs(n-b):
        return abs(n-b)
    else:
        return abs(n-a)
n=int(input())
if op(n):
    print(0)
else:
    print(k(n))