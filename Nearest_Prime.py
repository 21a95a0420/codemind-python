def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def komal(x):
    a=x
    b=x
    while prime(a)==False:
        a=a-1
    while prime(b)==False:
        b=b+1
    if abs(x-a)>abs(x-b):
        return b
    else:
        return a
n=int(input())
for i in range(n):
    a=int(input())
    print(komal(a))