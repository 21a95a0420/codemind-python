import math
n=int(input())
temp=n
c=0
while n:
    a=n%10
    c+=math.factorial(a)
    n=n//10
if temp==c:
    print("The number {} is a strong number".format(temp))
else:
    print("The number {} is not a strong number".format(temp))
   