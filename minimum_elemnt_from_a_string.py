a=input().split()
a=a[-1]
b="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
c=[]
for i in a:
    if i in b:
        c.append(i)
d=min(c)
e=d.lower()
if e in a:
    print(e)
else:
    print(d)