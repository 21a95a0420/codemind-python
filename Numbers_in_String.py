n=input()
s=0
for i in n:
    if i.isdigit():
        i=int(i)
        s+=i
print(s)