
"""Given an ordered array with repeated list the find occurence of the repeated element
   Complexity : O(l), where l = N-non-repeated elements. Computation will take as much as repeated element time.
"""

def repeatableElementCount(array,n,**kwargs):
    """ Option 1: Using recursion """
    if(option==1):
        if(n<0):
            pass
        else:
            if(array[n]-array[n-1])==0:
                    repeatableElementCount.c+=1
            return repeatableElementCount(array,n-1), repeatableElementCount.c
    """ Option 2: Using xrange """
    if(option==2):
        for x in xrange(len(array)-1):
            y = x
            while array[y] == array[y+1]:
                repeatableElementCount.l+=1
                y+=1
            if y !=x:
                break
        return repeatableElementCount.l



repeatableElementCount.c=1
repeatableElementCount.l=0
t = [1,1,1,1,1,1,1,1,2,3]
option=1
a= repeatableElementCount(t, n=len(t)-1,option=2)
print(a)



