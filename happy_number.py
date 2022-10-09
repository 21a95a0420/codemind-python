def lol(x):
    s=0
    while x:
        c=x%10
        s+=c*c
        x=x//10
    if s<9:
        return s
    else:
        return lol(s)
n=int(input())
if lol(n)==1 or lol(n)==7:
    print('True')
else:
    print('False')