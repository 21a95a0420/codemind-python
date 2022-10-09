a,b=map(int,input().split())
c=min(a,b)
while 1:
    if c%a==0 and c%b==0:
        print(c)
        break
    c=c+1
