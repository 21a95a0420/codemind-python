def pal(n):
    r=0
    while n:
        s=n%10
        r=r*10+s
        n=n//10
    return r
def rev(y):
    if y==pal(y):
        return True
    return False
def k(c):
    a=c+1
    b=c-1
    while rev(a)==False:
        a+=1
    while rev(b)==False:
        b-=1
    if abs(c-a)==abs(c-b):
        return (str(b)+" "+str(a))
    elif abs(c-a)>abs(c-b):
        return b
    else: return a
    
    
n=int(input())
print(k(n))
    