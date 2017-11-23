
#a = [1,2,4,3]
a = [6,8,9,2]
l = len(a)


"""Given an unordered array write an algorithm to sort the element array in ascending order.
   Constraint: * Only use recursion * Only use WHILE/IF loop
   Complexity : O(2) per swap
"""
def sort_recursion(a,i,d,l):
    if d==3:
        return a
    else:
        head = a[i]
        j = i+1# genius !!!
        while j<l:
            if (head - a[j]<0):
                j+=1
                continue
            if(head - a[j]>0):
                a[i],a[j] = a[j], a[i] # swap
                sort_recursion.swapCount+=1 # swap counter
                j+=1
        return sort_recursion(a,i+1,d+1,l)

sort_recursion.swapCount=0

c = sort_recursion(a,0,0,l)
print(c)
print(sort_recursion.swapCount) # Case a = [6,8,9,2] Swap count : 3

