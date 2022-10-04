n=int(input())
lst=list(map(int,input().split()))
a=[]
c=0
for i in lst:
    if i==lst.count(i):
        a.append(i)
        c=1
if c==0:
    print(-1)
else:
    print(min(a),max(a))
    
    
