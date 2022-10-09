a=int(input())
b=a*a
a=str(a)
b=str(b)
c=len(a)
if a==b[-c:]:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')