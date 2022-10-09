n=int(input())
k=n*n
n1=str(n)[::-1]
n2=int(n1)
n3=n2*n2
if str(k)==str(n3)[::-1]:
    print('True')
else:
    print('False')