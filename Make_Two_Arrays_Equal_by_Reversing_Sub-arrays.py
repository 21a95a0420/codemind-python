n=int(input())
k=list(map(int,input().split()))
b=int(input())
a=list(map(int,input().split()))[::-1]
print(sorted(k)==sorted(a))