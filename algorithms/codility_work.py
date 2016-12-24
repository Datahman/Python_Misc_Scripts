# Codility work
# 1 Find missing number in an array.


def solution(A):
    # Assume missing element has been added to array A.
    actual_length = len(A) + 1 
    # This is the expected sum of array size == (actual_length). i.e for (n * (n+1) / 2)
    exp_sum = (( actual_length) * ( actual_length + 1)) / (2) 
    # Actual sum.
    sum = 0 # Initialise sum index.
    for idx in range(0,len(A)):
        sum += A[idx]
    # Thus, missing element is: 
    return exp_sum - sum
#print(solution([2,3,1,5]))


# Leap frog problem

def lp(X, Y, D):
    
    # Raise execeptiona at case:  X > Y
    if (X > Y) or (D <= 0):
        raise Exception("Invalid arguements")
    # Case of integer division with no remainder.
    if ( Y - X ) % D == 0:
        no_jump = (Y - X ) / D
        return no_jump
    if ( Y -  X ) % D != 0:
        no_jump = (Y - X ) / D + 1
        return no_jump
    
#print(lp(1,5,2))

# Problem 3:
# Return minimumof a given array using tape_equilbiirum algorithm.
difference_list_L = []
difference_list_R = []
temp_ = []

def tape_algo(A):
    sumL = 0
    sumR = 0
    for idc in range(len(A)-1):
        sumL+= A[idc]
        difference_list_L.append(sumL)
    print "###"
    for j in range(1,len(A)):
        #counter +=1
        sumR = sum(A[j:len(A)])
        difference_list_R.append(sumR)
    for ix in range(0,4):
        difference = abs(difference_list_R[ix] - difference_list_L[ix])
        temp_.append(difference)
    return (min(temp_))
    #jth_index = len(A) - 1
    #ith_part = 0 
    #for i in range(len(A)):
    #    count=0
    #    for j in range(1,len(A)):
    #        count+=1
    #        difference_index=  j - count
    #        print difference_index
    #    
    #for i in range(len(A)):
    #    for j in range (1,len(A)):
    #        if i ==0:
    #            
    #            ith_part = A[i]
    #        if i !=0:
    #            ith_part += A[j] 
    #        jth_part +=  A[j]
    #        difference = abs(ith_part - jth_part)  
    #    print difference, i,ith_part, j
    #        #return None
#print(tape_algo([3,1,2,4,3]))


# Problem: Problem to think about

def isperm(A):
    def decorator(*args, **kwargs):
        
        
        return  
    return decorator
#print(isperm([4,1,3,2]))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
some = []        
for t in range(1,5+1):
    some.append(fact(t))
#print(some)


# Check a given zero indexed array is permutable or not.
# To do: Make it work for negative elements.
# Codility score: 70%
import random
import cProfile
def perm(A):
    if len(A) == 0:
        raise Exception ("No list provided!")
    else:
        random.shuffle(A)
        print A
        Size_A = len(A)
        actual_sum = sum(A)
        expected_sum = (Size_A) * (Size_A +1) / 2   
        if (expected_sum) == (actual_sum):
            return 1
        else:
            return 0
print(perm([x for x in range(1,10)])) # Checks: permutable array.
print(perm([3,2,4])) # Checks: permutable array.
print(perm([]))# Sanity check

#cProfile.run('perm([random.randrange(1,101,1) for x in range(random.randrange(1,10))])')

#Note: Why does this fail: A = random.shuffle(A).




## Use stacking mechanism to add/ multiple a given string.



stack = []

def sol(a):
    if len(a) == 0 or len(a) == None:
        return -1
    
    else:
        range_ = len(a)
        for i in range(range_):
            if a[i].isdigit(): # Digit case
                stack.append(a[i]) 
                
            elif len(stack) >= 0: # Operator case
                if a[i] == '+':
                    result = int(stack.pop()) + int(stack.pop())
                    stack.append(result)
                if a[i] == '*':
                    result = int(stack.pop()) * int(stack.pop())
                    stack.append(result)
            
        print stack
                    

    
    
print (sol('13+7+6*5*'))