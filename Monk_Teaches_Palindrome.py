for i in range(int(input())):
    a=input()
    if a!=a[::-1]:
        print('NO')
    elif a==a[::-1] and len(a)%2==0:
        print('YES EVEN')
    else:
        print('YES ODD')