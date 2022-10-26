n=input().split()
s=[]
for i in n:
    s.append(i[::-1])
print(*s)