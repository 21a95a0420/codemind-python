c=0
for i in input().lower().split():
    if i==i[::-1]:c+=1
print(c)