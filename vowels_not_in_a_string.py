a=input().lower()
k=["a","e","i","o","u"]
c=[]
d=[]
for i in k:
    if i  not in a:
        c.append(i)
if len(c)==0:
    print(0)
else:
    print(*c)