n=int(input())
k=n*n
s=0
while k:
    a=k%10
    s+=a
    k=k//10
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')