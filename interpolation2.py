L=[3,5,7,8,31,333,420]
target=8
least=0
high=len(L)-1

#using functional approach
def interpolation(L,target):
    least=0
    high=len(L)-1
    while least<=high and L[least]<=target<=L[high]:
        ind=int(least+((high-least)/(L[high]-L[least]))*(target-L[least]))
        if L[ind]<target:
            least=ind+1
        elif L[ind]>target:
            high=ind-1
        elif L[ind]==target:
            return ind
    return -1

print(interpolation(L,target))