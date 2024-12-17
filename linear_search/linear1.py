l=[12,43,897,-1,20,56,43,8]
target=int(input('enter target:'))
for i in range(len(l)):
    if l[i]==target:
        print(i)
        break
else:
    print(-1)
    
