def add(n):
    c=0
    while n:
        c+=n%10
        n//=10
    if c>9:
        return add(c)
    return c
print(add(int(input())))