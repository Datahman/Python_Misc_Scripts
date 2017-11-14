#
#em_ =[]
#stack = [] # Empty list to be used as a stack to accumulate all integers.
#def solution(S):
#    range_ = len(S)
#    
#    for ix in range(range_):
#        if S[ix].isdigit():
#            pop_(S[ix])
#        elif S[ix] == "+":
#            print(add_operator(stack))
#            loc_= ix
#        elif S[ix] == "*":
#
#            mult_loc = S[ix - 1] # Provides the result of addition.
#            mult_loc = int(mult_loc)
#            #print (mult_operator())
#            #print em_[-1]
#            print(mult_operator(em_[-1],mult_loc))
#                        
#def pop_(a):
#    a = int(a)
#    stack.append(a)
#    return stack
#
#def add_operator(stack):
#    add_result = 0
#    for i in range(len(stack)):
#        add_result += stack[i]
#    em_.append(add_result)
#    return add_result
#
#def mult_operator(add_result, mult_loc):
#    mult_result = add_result * mult_loc
#    return mult_result
#
##def print_final_result():
##    final_result = mult_result
##    string_ = "Final result with multiplcation included is: "
##    print '%s %s' % (string_,final_result) 
##    return final_result
#print(solution('13+7+6*'))            
#
## To do add two stacks, one for add other for mult.



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