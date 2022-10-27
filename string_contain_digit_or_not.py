k=input()
s='0123456789'
l=0
for i in k:
    if i in s:
        l+=1
if l!=0:
    print("Contains",l,"digit")
else:
    print("Doesn't contain digit")