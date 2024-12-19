L=[3,5,7,8,31,333,420]
target=8
least=0
high=len(L)-1

#using recursion
def intpol(L,target,least,high):
    if L[least]>target or L[high]<target or least>high:
        return -1
    ind=int(least+((high-least)/(L[high]-L[least]))*(target-L[least]))
    if L[ind]<target:
        least=ind+1
    elif L[ind]>target:
        high=ind-1
    elif L[ind]==target:
        return ind
    return intpol(L,target,least,high)

print(intpol(L,target,0,len(L)-1))