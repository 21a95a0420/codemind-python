n=int(input())
k=list(map(int,input().split()))
s=sorted(k)
if k==s[::-1]:
    print('yes')
else:
    print('no')