n=int(input())
for i in range(0,2**n):
    s=bin(i)[2:]
    k=n-len(s)
    print('0'*k+s)