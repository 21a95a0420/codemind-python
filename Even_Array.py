n=int(input())
k=list(map(int,input().split()))
for i in k:
    if i%2==1:
        print('False')
        break
else:
    print('True')