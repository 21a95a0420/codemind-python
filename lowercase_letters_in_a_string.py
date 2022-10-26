a=input()
b="qwertyuiopasdfghjklzxcvbnm"
s=0
for i in a:
    if i in b:
        s+=1
print(s)