n=int(input())
for i in range(n):
    a=input()
    k=a[::-1]
    if a==k:
        print('True')
    else:
        print('False')