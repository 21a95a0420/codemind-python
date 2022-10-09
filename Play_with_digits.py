n=int(input())
x=list(map(int,input().split()))
l=0
for i in x:
    s=i
    c=0
    while s:
        a=s%10
        c+=a
        s=s//10
    l+=c
print(l)