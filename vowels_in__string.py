a=input()
k=["a","e","i","o","u","A","E","I","O","U"]
c=[]
d=[]
for i in a:
    if i in k:
        c.append(i)
for j in c:
    if j not in d:
        d.append(j)
if len(d)==0:
    print(-1)
else:
    print(*d)
