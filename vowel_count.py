a=input()
k=["a","e","i","o","u","A","E","I","O","U"]
c=[]
d=[]
for i in a:
    if i in k:
        c.append(i)
print(len(c))
