n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=input()
    t=b
    for i in range(b,0,-1):
        k=s[:t][::-1]
        s=k+s[t:]
        t-=1
    print(s)
        