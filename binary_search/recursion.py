l=[12,43,897,-1,20,56,43,8]
target=int(input())
s=set(l)
l=list(s)
l.sort()
print(l)
low=0
high=len(l)-1
def binary(l,target,low,high):
    ind=(low+high)//2
    if l[ind]<target:
        low=ind+1
    elif l[ind]>target:
        high=ind-1
    elif l[ind]==target:
        return ind
    return binary(l,target,low,high)

print(binary(l,target,low,high))
