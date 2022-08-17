n=int(input())
a=0
b=1
while n>0:
    c=n%10
    a=a+c
    b=b*c
    n=n//10
if a==b:
    print("Spy Number")
else:
    print("Not Spy Number")