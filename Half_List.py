import math
n=int(input())
k=list(map(int,input().split()))
l=math.ceil(len(k)//2)
m=k[:l]
o=k[l:]
print(*(o[::-1]+m))
